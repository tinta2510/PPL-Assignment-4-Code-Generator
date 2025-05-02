# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0293\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3\u00bb\n\3\f\3\16\3\u00be\13\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00c9\n\5\3\6\3\6\3\6\3\6\5\6\u00cf")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d9\n\7\3\b")
        buf.write("\3\b\5\b\u00dd\n\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00f1\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\5\20\u00fb")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0105")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u010d\n\22\f")
        buf.write("\22\16\22\u0110\13\22\3\23\3\23\3\23\3\23\3\24\3\24\5")
        buf.write("\24\u0118\n\24\3\25\3\25\3\25\3\25\3\25\7\25\u011f\n\25")
        buf.write("\f\25\16\25\u0122\13\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\5\33\u013c\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\7\34\u0143\n\34\f\34\16\34\u0146")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \5 \u0157\n \3!\3!\3!\3!\3!\7")
        buf.write("!\u015e\n!\f!\16!\u0161\13!\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0173\n$\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\7&\u0180\n&\f&\16&\u0183\13&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\5+\u0197")
        buf.write("\n+\3,\3,\3,\3,\5,\u019d\n,\3,\3,\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\5/\u01ab\n/\3\60\3\60\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u01c9\n\67\38\38\38\58\u01ce\n8\39\39\39\59\u01d3")
        buf.write("\n9\3:\3:\3:\3:\3:\3:\5:\u01db\n:\3;\3;\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u01ec\n=\3>\3>\5>\u01f0\n")
        buf.write(">\3?\3?\3@\3@\3@\3@\3A\3A\5A\u01fa\nA\3B\3B\3B\3B\3B\5")
        buf.write("B\u0201\nB\3C\3C\3C\3C\5C\u0207\nC\3D\3D\3D\3E\3E\3F\3")
        buf.write("F\3F\3F\3G\3G\5G\u0214\nG\3H\3H\3H\3H\3H\5H\u021b\nH\3")
        buf.write("I\3I\3I\3I\3J\3J\3K\3K\3L\3L\3L\3L\3L\3L\7L\u022b\nL\f")
        buf.write("L\16L\u022e\13L\3M\3M\3M\3M\3M\3M\7M\u0236\nM\fM\16M\u0239")
        buf.write("\13M\3N\3N\3N\3N\3N\3N\7N\u0241\nN\fN\16N\u0244\13N\3")
        buf.write("O\3O\3O\3O\3O\3O\7O\u024c\nO\fO\16O\u024f\13O\3P\3P\3")
        buf.write("P\3P\3P\3P\7P\u0257\nP\fP\16P\u025a\13P\3Q\3Q\3Q\5Q\u025f")
        buf.write("\nQ\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\7R\u026c\nR\fR\16")
        buf.write("R\u026f\13R\3S\3S\3S\3T\3T\3T\3T\3U\3U\3U\3U\3V\3V\5V")
        buf.write("\u027e\nV\3W\3W\3W\3W\3W\5W\u0285\nW\3X\3X\3X\3X\3X\3")
        buf.write("X\3X\3X\5X\u028f\nX\3Y\3Y\3Y\2\16\4\"(\66@J\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a2Z\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write("\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write("\2\n\4\2\17\22::\3\2*/\3\2;>\3\2 %\3\2\33\34\3\2\35\37")
        buf.write("\4\2\33\34((\4\2\3\399\2\u027c\2\u00b2\3\2\2\2\4\u00b5")
        buf.write("\3\2\2\2\6\u00bf\3\2\2\2\b\u00c8\3\2\2\2\n\u00ce\3\2\2")
        buf.write("\2\f\u00d8\3\2\2\2\16\u00dc\3\2\2\2\20\u00de\3\2\2\2\22")
        buf.write("\u00e0\3\2\2\2\24\u00e3\3\2\2\2\26\u00e7\3\2\2\2\30\u00f0")
        buf.write("\3\2\2\2\32\u00f2\3\2\2\2\34\u00f6\3\2\2\2\36\u00fa\3")
        buf.write("\2\2\2 \u0104\3\2\2\2\"\u0106\3\2\2\2$\u0111\3\2\2\2&")
        buf.write("\u0117\3\2\2\2(\u0119\3\2\2\2*\u0123\3\2\2\2,\u0129\3")
        buf.write("\2\2\2.\u012e\3\2\2\2\60\u0130\3\2\2\2\62\u0135\3\2\2")
        buf.write("\2\64\u013b\3\2\2\2\66\u013d\3\2\2\28\u0147\3\2\2\2:\u014b")
        buf.write("\3\2\2\2<\u0150\3\2\2\2>\u0156\3\2\2\2@\u0158\3\2\2\2")
        buf.write("B\u0162\3\2\2\2D\u0166\3\2\2\2F\u0172\3\2\2\2H\u0174\3")
        buf.write("\2\2\2J\u0178\3\2\2\2L\u0184\3\2\2\2N\u0186\3\2\2\2P\u0188")
        buf.write("\3\2\2\2R\u018d\3\2\2\2T\u0196\3\2\2\2V\u0198\3\2\2\2")
        buf.write("X\u01a0\3\2\2\2Z\u01a2\3\2\2\2\\\u01aa\3\2\2\2^\u01ac")
        buf.write("\3\2\2\2`\u01b0\3\2\2\2b\u01b6\3\2\2\2d\u01b8\3\2\2\2")
        buf.write("f\u01ba\3\2\2\2h\u01bd\3\2\2\2j\u01bf\3\2\2\2l\u01c8\3")
        buf.write("\2\2\2n\u01cd\3\2\2\2p\u01d2\3\2\2\2r\u01da\3\2\2\2t\u01dc")
        buf.write("\3\2\2\2v\u01de\3\2\2\2x\u01eb\3\2\2\2z\u01ef\3\2\2\2")
        buf.write("|\u01f1\3\2\2\2~\u01f3\3\2\2\2\u0080\u01f9\3\2\2\2\u0082")
        buf.write("\u0200\3\2\2\2\u0084\u0206\3\2\2\2\u0086\u0208\3\2\2\2")
        buf.write("\u0088\u020b\3\2\2\2\u008a\u020d\3\2\2\2\u008c\u0213\3")
        buf.write("\2\2\2\u008e\u021a\3\2\2\2\u0090\u021c\3\2\2\2\u0092\u0220")
        buf.write("\3\2\2\2\u0094\u0222\3\2\2\2\u0096\u0224\3\2\2\2\u0098")
        buf.write("\u022f\3\2\2\2\u009a\u023a\3\2\2\2\u009c\u0245\3\2\2\2")
        buf.write("\u009e\u0250\3\2\2\2\u00a0\u025e\3\2\2\2\u00a2\u0260\3")
        buf.write("\2\2\2\u00a4\u0270\3\2\2\2\u00a6\u0273\3\2\2\2\u00a8\u0277")
        buf.write("\3\2\2\2\u00aa\u027d\3\2\2\2\u00ac\u0284\3\2\2\2\u00ae")
        buf.write("\u028e\3\2\2\2\u00b0\u0290\3\2\2\2\u00b2\u00b3\5\4\3\2")
        buf.write("\u00b3\u00b4\7\2\2\3\u00b4\3\3\2\2\2\u00b5\u00b6\b\3\1")
        buf.write("\2\u00b6\u00b7\5\6\4\2\u00b7\u00bc\3\2\2\2\u00b8\u00b9")
        buf.write("\f\3\2\2\u00b9\u00bb\5\6\4\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\5\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\5\b\5")
        buf.write("\2\u00c0\u00c1\5\u00b0Y\2\u00c1\7\3\2\2\2\u00c2\u00c9")
        buf.write("\5\n\6\2\u00c3\u00c9\5\24\13\2\u00c4\u00c9\5\26\f\2\u00c5")
        buf.write("\u00c9\5*\26\2\u00c6\u00c9\5\60\31\2\u00c7\u00c9\5:\36")
        buf.write("\2\u00c8\u00c2\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c8\u00c4")
        buf.write("\3\2\2\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\t\3\2\2\2\u00ca\u00cf\5\f\7\2\u00cb")
        buf.write("\u00cc\7\24\2\2\u00cc\u00cd\7:\2\2\u00cd\u00cf\5\16\b")
        buf.write("\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb\3\2\2\2\u00cf\13\3")
        buf.write("\2\2\2\u00d0\u00d1\7\24\2\2\u00d1\u00d2\7:\2\2\u00d2\u00d3")
        buf.write("\5\16\b\2\u00d3\u00d4\5\22\n\2\u00d4\u00d9\3\2\2\2\u00d5")
        buf.write("\u00d6\7\24\2\2\u00d6\u00d7\7:\2\2\u00d7\u00d9\5\22\n")
        buf.write("\2\u00d8\u00d0\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d9\r\3\2")
        buf.write("\2\2\u00da\u00dd\5\20\t\2\u00db\u00dd\5x=\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\17\3\2\2\2\u00de\u00df")
        buf.write("\t\2\2\2\u00df\21\3\2\2\2\u00e0\u00e1\7)\2\2\u00e1\u00e2")
        buf.write("\5\u0096L\2\u00e2\23\3\2\2\2\u00e3\u00e4\7\23\2\2\u00e4")
        buf.write("\u00e5\7:\2\2\u00e5\u00e6\5\22\n\2\u00e6\25\3\2\2\2\u00e7")
        buf.write("\u00e8\7\13\2\2\u00e8\u00e9\7:\2\2\u00e9\u00ea\5\30\r")
        buf.write("\2\u00ea\u00eb\5$\23\2\u00eb\27\3\2\2\2\u00ec\u00ed\5")
        buf.write("\32\16\2\u00ed\u00ee\5\34\17\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00f1\5\32\16\2\u00f0\u00ec\3\2\2\2\u00f0\u00ef\3\2\2")
        buf.write("\2\u00f1\31\3\2\2\2\u00f2\u00f3\7\62\2\2\u00f3\u00f4\5")
        buf.write("\36\20\2\u00f4\u00f5\7\63\2\2\u00f5\33\3\2\2\2\u00f6\u00f7")
        buf.write("\5\16\b\2\u00f7\35\3\2\2\2\u00f8\u00fb\5 \21\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("\37\3\2\2\2\u00fc\u00fd\5\"\22\2\u00fd\u00fe\5\16\b\2")
        buf.write("\u00fe\u00ff\78\2\2\u00ff\u0100\5 \21\2\u0100\u0105\3")
        buf.write("\2\2\2\u0101\u0102\5\"\22\2\u0102\u0103\5\16\b\2\u0103")
        buf.write("\u0105\3\2\2\2\u0104\u00fc\3\2\2\2\u0104\u0101\3\2\2\2")
        buf.write("\u0105!\3\2\2\2\u0106\u0107\b\22\1\2\u0107\u0108\7:\2")
        buf.write("\2\u0108\u010e\3\2\2\2\u0109\u010a\f\3\2\2\u010a\u010b")
        buf.write("\78\2\2\u010b\u010d\7:\2\2\u010c\u0109\3\2\2\2\u010d\u0110")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("#\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7\64\2\2\u0112")
        buf.write("\u0113\5&\24\2\u0113\u0114\7\65\2\2\u0114%\3\2\2\2\u0115")
        buf.write("\u0118\5(\25\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0117\u0116\3\2\2\2\u0118\'\3\2\2\2\u0119\u011a\b\25")
        buf.write("\1\2\u011a\u011b\5D#\2\u011b\u0120\3\2\2\2\u011c\u011d")
        buf.write("\f\3\2\2\u011d\u011f\5D#\2\u011e\u011c\3\2\2\2\u011f\u0122")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write(")\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7\13\2\2\u0124")
        buf.write("\u0125\5,\27\2\u0125\u0126\7:\2\2\u0126\u0127\5\30\r\2")
        buf.write("\u0127\u0128\5$\23\2\u0128+\3\2\2\2\u0129\u012a\7\62\2")
        buf.write("\2\u012a\u012b\7:\2\2\u012b\u012c\5.\30\2\u012c\u012d")
        buf.write("\7\63\2\2\u012d-\3\2\2\2\u012e\u012f\7:\2\2\u012f/\3\2")
        buf.write("\2\2\u0130\u0131\7\f\2\2\u0131\u0132\7:\2\2\u0132\u0133")
        buf.write("\7\r\2\2\u0133\u0134\5\62\32\2\u0134\61\3\2\2\2\u0135")
        buf.write("\u0136\7\64\2\2\u0136\u0137\5\64\33\2\u0137\u0138\7\65")
        buf.write("\2\2\u0138\63\3\2\2\2\u0139\u013c\5\66\34\2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013a\3\2\2\2\u013c")
        buf.write("\65\3\2\2\2\u013d\u013e\b\34\1\2\u013e\u013f\58\35\2\u013f")
        buf.write("\u0144\3\2\2\2\u0140\u0141\f\3\2\2\u0141\u0143\58\35\2")
        buf.write("\u0142\u0140\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3")
        buf.write("\2\2\2\u0144\u0145\3\2\2\2\u0145\67\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0147\u0148\7:\2\2\u0148\u0149\5\16\b\2\u0149")
        buf.write("\u014a\5\u00b0Y\2\u014a9\3\2\2\2\u014b\u014c\7\f\2\2\u014c")
        buf.write("\u014d\7:\2\2\u014d\u014e\7\16\2\2\u014e\u014f\5<\37\2")
        buf.write("\u014f;\3\2\2\2\u0150\u0151\7\64\2\2\u0151\u0152\5> \2")
        buf.write("\u0152\u0153\7\65\2\2\u0153=\3\2\2\2\u0154\u0157\5@!\2")
        buf.write("\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3")
        buf.write("\2\2\2\u0157?\3\2\2\2\u0158\u0159\b!\1\2\u0159\u015a\5")
        buf.write("B\"\2\u015a\u015f\3\2\2\2\u015b\u015c\f\3\2\2\u015c\u015e")
        buf.write("\5B\"\2\u015d\u015b\3\2\2\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160A\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0163\7:\2\2\u0163\u0164\5\30\r\2")
        buf.write("\u0164\u0165\5\u00b0Y\2\u0165C\3\2\2\2\u0166\u0167\5F")
        buf.write("$\2\u0167\u0168\5\u00b0Y\2\u0168E\3\2\2\2\u0169\u0173")
        buf.write("\5\n\6\2\u016a\u0173\5\24\13\2\u016b\u0173\5H%\2\u016c")
        buf.write("\u0173\5P)\2\u016d\u0173\5V,\2\u016e\u0173\5h\65\2\u016f")
        buf.write("\u0173\5j\66\2\u0170\u0173\5l\67\2\u0171\u0173\5n8\2\u0172")
        buf.write("\u0169\3\2\2\2\u0172\u016a\3\2\2\2\u0172\u016b\3\2\2\2")
        buf.write("\u0172\u016c\3\2\2\2\u0172\u016d\3\2\2\2\u0172\u016e\3")
        buf.write("\2\2\2\u0172\u016f\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173G\3\2\2\2\u0174\u0175\5J&\2\u0175\u0176")
        buf.write("\5L\'\2\u0176\u0177\5N(\2\u0177I\3\2\2\2\u0178\u0179\b")
        buf.write("&\1\2\u0179\u017a\7:\2\2\u017a\u0181\3\2\2\2\u017b\u017c")
        buf.write("\f\4\2\2\u017c\u0180\5\u00a4S\2\u017d\u017e\f\3\2\2\u017e")
        buf.write("\u0180\5\u00a6T\2\u017f\u017b\3\2\2\2\u017f\u017d\3\2")
        buf.write("\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182")
        buf.write("\3\2\2\2\u0182K\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185")
        buf.write("\t\3\2\2\u0185M\3\2\2\2\u0186\u0187\5\u0096L\2\u0187O")
        buf.write("\3\2\2\2\u0188\u0189\7\7\2\2\u0189\u018a\5R*\2\u018a\u018b")
        buf.write("\5$\23\2\u018b\u018c\5T+\2\u018cQ\3\2\2\2\u018d\u018e")
        buf.write("\7\62\2\2\u018e\u018f\5\u0096L\2\u018f\u0190\7\63\2\2")
        buf.write("\u0190S\3\2\2\2\u0191\u0192\7\b\2\2\u0192\u0197\5$\23")
        buf.write("\2\u0193\u0194\7\b\2\2\u0194\u0197\5P)\2\u0195\u0197\3")
        buf.write("\2\2\2\u0196\u0191\3\2\2\2\u0196\u0193\3\2\2\2\u0196\u0195")
        buf.write("\3\2\2\2\u0197U\3\2\2\2\u0198\u019c\7\t\2\2\u0199\u019d")
        buf.write("\5X-\2\u019a\u019d\5Z.\2\u019b\u019d\5`\61\2\u019c\u0199")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\5$\23\2\u019fW\3\2\2\2\u01a0")
        buf.write("\u01a1\5\u0096L\2\u01a1Y\3\2\2\2\u01a2\u01a3\5\\/\2\u01a3")
        buf.write("\u01a4\79\2\2\u01a4\u01a5\5X-\2\u01a5\u01a6\79\2\2\u01a6")
        buf.write("\u01a7\5^\60\2\u01a7[\3\2\2\2\u01a8\u01ab\5^\60\2\u01a9")
        buf.write("\u01ab\5\f\7\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2")
        buf.write("\u01ab]\3\2\2\2\u01ac\u01ad\7:\2\2\u01ad\u01ae\5L\'\2")
        buf.write("\u01ae\u01af\5\u0096L\2\u01af_\3\2\2\2\u01b0\u01b1\5b")
        buf.write("\62\2\u01b1\u01b2\78\2\2\u01b2\u01b3\5d\63\2\u01b3\u01b4")
        buf.write("\7*\2\2\u01b4\u01b5\5f\64\2\u01b5a\3\2\2\2\u01b6\u01b7")
        buf.write("\7:\2\2\u01b7c\3\2\2\2\u01b8\u01b9\7:\2\2\u01b9e\3\2\2")
        buf.write("\2\u01ba\u01bb\7\27\2\2\u01bb\u01bc\5\u0096L\2\u01bcg")
        buf.write("\3\2\2\2\u01bd\u01be\7\26\2\2\u01bei\3\2\2\2\u01bf\u01c0")
        buf.write("\7\25\2\2\u01c0k\3\2\2\2\u01c1\u01c2\7:\2\2\u01c2\u01c9")
        buf.write("\5\u00a8U\2\u01c3\u01c4\5\u00a2R\2\u01c4\u01c5\7\60\2")
        buf.write("\2\u01c5\u01c6\7:\2\2\u01c6\u01c7\5\u00a8U\2\u01c7\u01c9")
        buf.write("\3\2\2\2\u01c8\u01c1\3\2\2\2\u01c8\u01c3\3\2\2\2\u01c9")
        buf.write("m\3\2\2\2\u01ca\u01cb\7\n\2\2\u01cb\u01ce\5\u0096L\2\u01cc")
        buf.write("\u01ce\7\n\2\2\u01cd\u01ca\3\2\2\2\u01cd\u01cc\3\2\2\2")
        buf.write("\u01ceo\3\2\2\2\u01cf\u01d3\5r:\2\u01d0\u01d3\5v<\2\u01d1")
        buf.write("\u01d3\5\u0086D\2\u01d2\u01cf\3\2\2\2\u01d2\u01d0\3\2")
        buf.write("\2\2\u01d2\u01d1\3\2\2\2\u01d3q\3\2\2\2\u01d4\u01db\5")
        buf.write("t;\2\u01d5\u01db\7?\2\2\u01d6\u01db\7@\2\2\u01d7\u01db")
        buf.write("\7\31\2\2\u01d8\u01db\7\32\2\2\u01d9\u01db\7\30\2\2\u01da")
        buf.write("\u01d4\3\2\2\2\u01da\u01d5\3\2\2\2\u01da\u01d6\3\2\2\2")
        buf.write("\u01da\u01d7\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3")
        buf.write("\2\2\2\u01dbs\3\2\2\2\u01dc\u01dd\t\4\2\2\u01ddu\3\2\2")
        buf.write("\2\u01de\u01df\5x=\2\u01df\u01e0\5~@\2\u01e0w\3\2\2\2")
        buf.write("\u01e1\u01e2\7\66\2\2\u01e2\u01e3\5z>\2\u01e3\u01e4\7")
        buf.write("\67\2\2\u01e4\u01e5\5x=\2\u01e5\u01ec\3\2\2\2\u01e6\u01e7")
        buf.write("\7\66\2\2\u01e7\u01e8\5z>\2\u01e8\u01e9\7\67\2\2\u01e9")
        buf.write("\u01ea\5\20\t\2\u01ea\u01ec\3\2\2\2\u01eb\u01e1\3\2\2")
        buf.write("\2\u01eb\u01e6\3\2\2\2\u01ecy\3\2\2\2\u01ed\u01f0\5t;")
        buf.write("\2\u01ee\u01f0\7:\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0{\3\2\2\2\u01f1\u01f2\5\20\t\2\u01f2}\3")
        buf.write("\2\2\2\u01f3\u01f4\7\64\2\2\u01f4\u01f5\5\u0080A\2\u01f5")
        buf.write("\u01f6\7\65\2\2\u01f6\177\3\2\2\2\u01f7\u01fa\5\u0082")
        buf.write("B\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fa\u0081\3\2\2\2\u01fb\u01fc\5\u0084C\2\u01fc")
        buf.write("\u01fd\78\2\2\u01fd\u01fe\5\u0082B\2\u01fe\u0201\3\2\2")
        buf.write("\2\u01ff\u0201\5\u0084C\2\u0200\u01fb\3\2\2\2\u0200\u01ff")
        buf.write("\3\2\2\2\u0201\u0083\3\2\2\2\u0202\u0207\7:\2\2\u0203")
        buf.write("\u0207\5r:\2\u0204\u0207\5\u0086D\2\u0205\u0207\5~@\2")
        buf.write("\u0206\u0202\3\2\2\2\u0206\u0203\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0206\u0205\3\2\2\2\u0207\u0085\3\2\2\2\u0208\u0209")
        buf.write("\5\u0088E\2\u0209\u020a\5\u008aF\2\u020a\u0087\3\2\2\2")
        buf.write("\u020b\u020c\7:\2\2\u020c\u0089\3\2\2\2\u020d\u020e\7")
        buf.write("\64\2\2\u020e\u020f\5\u008cG\2\u020f\u0210\7\65\2\2\u0210")
        buf.write("\u008b\3\2\2\2\u0211\u0214\5\u008eH\2\u0212\u0214\3\2")
        buf.write("\2\2\u0213\u0211\3\2\2\2\u0213\u0212\3\2\2\2\u0214\u008d")
        buf.write("\3\2\2\2\u0215\u0216\5\u0090I\2\u0216\u0217\78\2\2\u0217")
        buf.write("\u0218\5\u008eH\2\u0218\u021b\3\2\2\2\u0219\u021b\5\u0090")
        buf.write("I\2\u021a\u0215\3\2\2\2\u021a\u0219\3\2\2\2\u021b\u008f")
        buf.write("\3\2\2\2\u021c\u021d\5\u0092J\2\u021d\u021e\7\61\2\2\u021e")
        buf.write("\u021f\5\u0094K\2\u021f\u0091\3\2\2\2\u0220\u0221\7:\2")
        buf.write("\2\u0221\u0093\3\2\2\2\u0222\u0223\5\u0096L\2\u0223\u0095")
        buf.write("\3\2\2\2\u0224\u0225\bL\1\2\u0225\u0226\5\u0098M\2\u0226")
        buf.write("\u022c\3\2\2\2\u0227\u0228\f\4\2\2\u0228\u0229\7\'\2\2")
        buf.write("\u0229\u022b\5\u0098M\2\u022a\u0227\3\2\2\2\u022b\u022e")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u0097\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\bM\1\2")
        buf.write("\u0230\u0231\5\u009aN\2\u0231\u0237\3\2\2\2\u0232\u0233")
        buf.write("\f\4\2\2\u0233\u0234\7&\2\2\u0234\u0236\5\u009aN\2\u0235")
        buf.write("\u0232\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u0099\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u023a\u023b\bN\1\2\u023b\u023c\5\u009cO\2\u023c")
        buf.write("\u0242\3\2\2\2\u023d\u023e\f\4\2\2\u023e\u023f\t\5\2\2")
        buf.write("\u023f\u0241\5\u009cO\2\u0240\u023d\3\2\2\2\u0241\u0244")
        buf.write("\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u009b\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u0246\bO\1\2")
        buf.write("\u0246\u0247\5\u009eP\2\u0247\u024d\3\2\2\2\u0248\u0249")
        buf.write("\f\4\2\2\u0249\u024a\t\6\2\2\u024a\u024c\5\u009eP\2\u024b")
        buf.write("\u0248\3\2\2\2\u024c\u024f\3\2\2\2\u024d\u024b\3\2\2\2")
        buf.write("\u024d\u024e\3\2\2\2\u024e\u009d\3\2\2\2\u024f\u024d\3")
        buf.write("\2\2\2\u0250\u0251\bP\1\2\u0251\u0252\5\u00a0Q\2\u0252")
        buf.write("\u0258\3\2\2\2\u0253\u0254\f\4\2\2\u0254\u0255\t\7\2\2")
        buf.write("\u0255\u0257\5\u00a0Q\2\u0256\u0253\3\2\2\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("\u009f\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\t\b\2\2")
        buf.write("\u025c\u025f\5\u00a0Q\2\u025d\u025f\5\u00a2R\2\u025e\u025b")
        buf.write("\3\2\2\2\u025e\u025d\3\2\2\2\u025f\u00a1\3\2\2\2\u0260")
        buf.write("\u0261\bR\1\2\u0261\u0262\5\u00aeX\2\u0262\u026d\3\2\2")
        buf.write("\2\u0263\u0264\f\5\2\2\u0264\u026c\5\u00a4S\2\u0265\u0266")
        buf.write("\f\4\2\2\u0266\u026c\5\u00a6T\2\u0267\u0268\f\3\2\2\u0268")
        buf.write("\u0269\7\60\2\2\u0269\u026a\7:\2\2\u026a\u026c\5\u00a8")
        buf.write("U\2\u026b\u0263\3\2\2\2\u026b\u0265\3\2\2\2\u026b\u0267")
        buf.write("\3\2\2\2\u026c\u026f\3\2\2\2\u026d\u026b\3\2\2\2\u026d")
        buf.write("\u026e\3\2\2\2\u026e\u00a3\3\2\2\2\u026f\u026d\3\2\2\2")
        buf.write("\u0270\u0271\7\60\2\2\u0271\u0272\7:\2\2\u0272\u00a5\3")
        buf.write("\2\2\2\u0273\u0274\7\66\2\2\u0274\u0275\5\u0096L\2\u0275")
        buf.write("\u0276\7\67\2\2\u0276\u00a7\3\2\2\2\u0277\u0278\7\62\2")
        buf.write("\2\u0278\u0279\5\u00aaV\2\u0279\u027a\7\63\2\2\u027a\u00a9")
        buf.write("\3\2\2\2\u027b\u027e\5\u00acW\2\u027c\u027e\3\2\2\2\u027d")
        buf.write("\u027b\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u00ab\3\2\2\2")
        buf.write("\u027f\u0280\5\u0096L\2\u0280\u0281\78\2\2\u0281\u0282")
        buf.write("\5\u00acW\2\u0282\u0285\3\2\2\2\u0283\u0285\5\u0096L\2")
        buf.write("\u0284\u027f\3\2\2\2\u0284\u0283\3\2\2\2\u0285\u00ad\3")
        buf.write("\2\2\2\u0286\u028f\5p9\2\u0287\u028f\7:\2\2\u0288\u0289")
        buf.write("\7:\2\2\u0289\u028f\5\u00a8U\2\u028a\u028b\7\62\2\2\u028b")
        buf.write("\u028c\5\u0096L\2\u028c\u028d\7\63\2\2\u028d\u028f\3\2")
        buf.write("\2\2\u028e\u0286\3\2\2\2\u028e\u0287\3\2\2\2\u028e\u0288")
        buf.write("\3\2\2\2\u028e\u028a\3\2\2\2\u028f\u00af\3\2\2\2\u0290")
        buf.write("\u0291\t\t\2\2\u0291\u00b1\3\2\2\2-\u00bc\u00c8\u00ce")
        buf.write("\u00d8\u00dc\u00f0\u00fa\u0104\u010e\u0117\u0120\u013b")
        buf.write("\u0144\u0156\u015f\u0172\u017f\u0181\u0196\u019c\u01aa")
        buf.write("\u01c8\u01cd\u01d2\u01da\u01eb\u01ef\u01f9\u0200\u0206")
        buf.write("\u0213\u021a\u022c\u0237\u0242\u024d\u0258\u025e\u026b")
        buf.write("\u026d\u027d\u0284\u028e")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "NL", "WS", "LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "PLUS", "MINUS", "STAR", "SLASH", 
                      "MOD", "EQUALS", "NOT_EQUALS", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "AND", "OR", 
                      "NOT", "ASSIGN", "COLON_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "STAR_ASSIGN", "SLASH_ASSIGN", "MOD_ASSIGN", "DOT", 
                      "COLON", "L_PAREN", "R_PAREN", "L_BRACE", "R_BRACE", 
                      "L_BRACKET", "R_BRACKET", "COMMA", "SEMICOLON", "IDENTIFIER", 
                      "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", "HEX_INT", 
                      "FLOAT_LIT", "STRING_LIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_declList = 1
    RULE_decl = 2
    RULE_declBody = 3
    RULE_varDecl = 4
    RULE_varDeclWithInit = 5
    RULE_type_ = 6
    RULE_basicTypeAndStruct = 7
    RULE_initilization = 8
    RULE_constDecl = 9
    RULE_funcDecl = 10
    RULE_signature = 11
    RULE_parameterList = 12
    RULE_returnType = 13
    RULE_parameterDeclList = 14
    RULE_nonNullParameterDeclList = 15
    RULE_identifierList = 16
    RULE_block = 17
    RULE_stmtList = 18
    RULE_nonNullStmtList = 19
    RULE_methodDefine = 20
    RULE_receiver = 21
    RULE_receiverType = 22
    RULE_structDecl = 23
    RULE_structBody = 24
    RULE_fieldDeclList = 25
    RULE_nonNullFieldDeclList = 26
    RULE_fieldDecl = 27
    RULE_interfaceDecl = 28
    RULE_interfaceBody = 29
    RULE_methodDeclList = 30
    RULE_nonNullMethodDeclList = 31
    RULE_methodDecl = 32
    RULE_stmt = 33
    RULE_stmtBody = 34
    RULE_assignStmt = 35
    RULE_lhs = 36
    RULE_assignOp = 37
    RULE_rhs = 38
    RULE_ifStmt = 39
    RULE_ifCondition = 40
    RULE_elseStmt = 41
    RULE_forStmt = 42
    RULE_forCondition = 43
    RULE_forLoop = 44
    RULE_forLoopInit = 45
    RULE_forLoopUpdate = 46
    RULE_forRange = 47
    RULE_forIndex = 48
    RULE_forValue = 49
    RULE_rangeExpr = 50
    RULE_breakStmt = 51
    RULE_continueStmt = 52
    RULE_callStmt = 53
    RULE_returnStmt = 54
    RULE_literal = 55
    RULE_basicLit = 56
    RULE_integerLit = 57
    RULE_arrayLit = 58
    RULE_arrayType = 59
    RULE_arrayTypeIndex = 60
    RULE_arrayElementType = 61
    RULE_arrayValue = 62
    RULE_arrayList = 63
    RULE_nonNullArrayList = 64
    RULE_arrayElement = 65
    RULE_structLit = 66
    RULE_structType = 67
    RULE_structValue = 68
    RULE_keyedElementList = 69
    RULE_nonNullKeyedElementList = 70
    RULE_keyedElement = 71
    RULE_key = 72
    RULE_element = 73
    RULE_expression = 74
    RULE_logAndExpr = 75
    RULE_relExpr = 76
    RULE_addExpr = 77
    RULE_mulExpr = 78
    RULE_unaryExpr = 79
    RULE_primaryExpr = 80
    RULE_fieldAccess = 81
    RULE_arrayAccess = 82
    RULE_arguments = 83
    RULE_argumentList = 84
    RULE_nonNullArgumentList = 85
    RULE_operand = 86
    RULE_eos = 87

    ruleNames =  [ "program", "declList", "decl", "declBody", "varDecl", 
                   "varDeclWithInit", "type_", "basicTypeAndStruct", "initilization", 
                   "constDecl", "funcDecl", "signature", "parameterList", 
                   "returnType", "parameterDeclList", "nonNullParameterDeclList", 
                   "identifierList", "block", "stmtList", "nonNullStmtList", 
                   "methodDefine", "receiver", "receiverType", "structDecl", 
                   "structBody", "fieldDeclList", "nonNullFieldDeclList", 
                   "fieldDecl", "interfaceDecl", "interfaceBody", "methodDeclList", 
                   "nonNullMethodDeclList", "methodDecl", "stmt", "stmtBody", 
                   "assignStmt", "lhs", "assignOp", "rhs", "ifStmt", "ifCondition", 
                   "elseStmt", "forStmt", "forCondition", "forLoop", "forLoopInit", 
                   "forLoopUpdate", "forRange", "forIndex", "forValue", 
                   "rangeExpr", "breakStmt", "continueStmt", "callStmt", 
                   "returnStmt", "literal", "basicLit", "integerLit", "arrayLit", 
                   "arrayType", "arrayTypeIndex", "arrayElementType", "arrayValue", 
                   "arrayList", "nonNullArrayList", "arrayElement", "structLit", 
                   "structType", "structValue", "keyedElementList", "nonNullKeyedElementList", 
                   "keyedElement", "key", "element", "expression", "logAndExpr", 
                   "relExpr", "addExpr", "mulExpr", "unaryExpr", "primaryExpr", 
                   "fieldAccess", "arrayAccess", "arguments", "argumentList", 
                   "nonNullArgumentList", "operand", "eos" ]

    EOF = Token.EOF
    NL=1
    WS=2
    LINE_COMMENT=3
    MULTI_LINE_COMMENT=4
    IF=5
    ELSE=6
    FOR=7
    RETURN=8
    FUNC=9
    TYPE=10
    STRUCT=11
    INTERFACE=12
    STRING=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    NIL=22
    TRUE=23
    FALSE=24
    PLUS=25
    MINUS=26
    STAR=27
    SLASH=28
    MOD=29
    EQUALS=30
    NOT_EQUALS=31
    LESS_THAN=32
    LESS_THAN_OR_EQUAL=33
    GREATER_THAN=34
    GREATER_THAN_OR_EQUAL=35
    AND=36
    OR=37
    NOT=38
    ASSIGN=39
    COLON_ASSIGN=40
    PLUS_ASSIGN=41
    MINUS_ASSIGN=42
    STAR_ASSIGN=43
    SLASH_ASSIGN=44
    MOD_ASSIGN=45
    DOT=46
    COLON=47
    L_PAREN=48
    R_PAREN=49
    L_BRACE=50
    R_BRACE=51
    L_BRACKET=52
    R_BRACKET=53
    COMMA=54
    SEMICOLON=55
    IDENTIFIER=56
    DECIMAL_INT=57
    BINARY_INT=58
    OCTAL_INT=59
    HEX_INT=60
    FLOAT_LIT=61
    STRING_LIT=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.declList(0)
            self.state = 177
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclList" ):
                return visitor.visitDeclList(self)
            else:
                return visitor.visitChildren(self)



    def declList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.DeclListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_declList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.DeclListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declList)
                    self.state = 182
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 183
                    self.decl() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declBody(self):
            return self.getTypedRuleContext(MiniGoParser.DeclBodyContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.declBody()
            self.state = 190
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def methodDefine(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDefineContext,0)


        def structDecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclContext,0)


        def interfaceDecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclBody" ):
                return visitor.visitDeclBody(self)
            else:
                return visitor.visitChildren(self)




    def declBody(self):

        localctx = MiniGoParser.DeclBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declBody)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.constDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.funcDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.methodDefine()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.structDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.interfaceDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclWithInit(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclWithInitContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.varDeclWithInit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(MiniGoParser.VAR)
                self.state = 202
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 203
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclWithInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def initilization(self):
            return self.getTypedRuleContext(MiniGoParser.InitilizationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclWithInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithInit" ):
                return visitor.visitVarDeclWithInit(self)
            else:
                return visitor.visitChildren(self)




    def varDeclWithInit(self):

        localctx = MiniGoParser.VarDeclWithInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclWithInit)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MiniGoParser.VAR)
                self.state = 207
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 208
                self.type_()
                self.state = 209
                self.initilization()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(MiniGoParser.VAR)
                self.state = 212
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 213
                self.initilization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicTypeAndStruct(self):
            return self.getTypedRuleContext(MiniGoParser.BasicTypeAndStructContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.basicTypeAndStruct()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.arrayType()
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


    class BasicTypeAndStructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basicTypeAndStruct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicTypeAndStruct" ):
                return visitor.visitBasicTypeAndStruct(self)
            else:
                return visitor.visitChildren(self)




    def basicTypeAndStruct(self):

        localctx = MiniGoParser.BasicTypeAndStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_basicTypeAndStruct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitilizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initilization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitilization" ):
                return visitor.visitInitilization(self)
            else:
                return visitor.visitChildren(self)




    def initilization(self):

        localctx = MiniGoParser.InitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.ASSIGN)
            self.state = 223
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def initilization(self):
            return self.getTypedRuleContext(MiniGoParser.InitilizationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.CONST)
            self.state = 226
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 227
            self.initilization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.FUNC)
            self.state = 230
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self.signature()
            self.state = 232
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterList(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterListContext,0)


        def returnType(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = MiniGoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_signature)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.parameterList()
                self.state = 235
                self.returnType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.parameterList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def parameterDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterDeclListContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = MiniGoParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.L_PAREN)
            self.state = 241
            self.parameterDeclList()
            self.state = 242
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = MiniGoParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullParameterDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullParameterDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterDeclList" ):
                return visitor.visitParameterDeclList(self)
            else:
                return visitor.visitChildren(self)




    def parameterDeclList(self):

        localctx = MiniGoParser.ParameterDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameterDeclList)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.nonNullParameterDeclList()
                pass
            elif token in [MiniGoParser.R_PAREN]:
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


    class NonNullParameterDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nonNullParameterDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullParameterDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullParameterDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullParameterDeclList" ):
                return visitor.visitNonNullParameterDeclList(self)
            else:
                return visitor.visitChildren(self)




    def nonNullParameterDeclList(self):

        localctx = MiniGoParser.NonNullParameterDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nonNullParameterDeclList)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.identifierList(0)
                self.state = 251
                self.type_()
                self.state = 252
                self.match(MiniGoParser.COMMA)
                self.state = 253
                self.nonNullParameterDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.identifierList(0)
                self.state = 256
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)



    def identifierList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_identifierList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MiniGoParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.IdentifierListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifierList)
                    self.state = 263
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 264
                    self.match(MiniGoParser.COMMA)
                    self.state = 265
                    self.match(MiniGoParser.IDENTIFIER) 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def stmtList(self):
            return self.getTypedRuleContext(MiniGoParser.StmtListContext,0)


        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.L_BRACE)
            self.state = 272
            self.stmtList()
            self.state = 273
            self.match(MiniGoParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullStmtList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullStmtListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = MiniGoParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtList)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.nonNullStmtList(0)
                pass
            elif token in [MiniGoParser.R_BRACE]:
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


    class NonNullStmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def nonNullStmtList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullStmtListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullStmtList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullStmtList" ):
                return visitor.visitNonNullStmtList(self)
            else:
                return visitor.visitChildren(self)



    def nonNullStmtList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.NonNullStmtListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_nonNullStmtList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.stmt()
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NonNullStmtListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_nonNullStmtList)
                    self.state = 282
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 283
                    self.stmt() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MethodDefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDefine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDefine" ):
                return visitor.visitMethodDefine(self)
            else:
                return visitor.visitChildren(self)




    def methodDefine(self):

        localctx = MiniGoParser.MethodDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_methodDefine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(MiniGoParser.FUNC)
            self.state = 290
            self.receiver()
            self.state = 291
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 292
            self.signature()
            self.state = 293
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def receiverType(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverTypeContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MiniGoParser.L_PAREN)
            self.state = 296
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 297
            self.receiverType()
            self.state = 298
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiverType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiverType" ):
                return visitor.visitReceiverType(self)
            else:
                return visitor.visitChildren(self)




    def receiverType(self):

        localctx = MiniGoParser.ReceiverTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_receiverType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def structBody(self):
            return self.getTypedRuleContext(MiniGoParser.StructBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = MiniGoParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.TYPE)
            self.state = 303
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 304
            self.match(MiniGoParser.STRUCT)
            self.state = 305
            self.structBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclListContext,0)


        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBody" ):
                return visitor.visitStructBody(self)
            else:
                return visitor.visitChildren(self)




    def structBody(self):

        localctx = MiniGoParser.StructBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_structBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.L_BRACE)
            self.state = 308
            self.fieldDeclList()
            self.state = 309
            self.match(MiniGoParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullFieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullFieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclList" ):
                return visitor.visitFieldDeclList(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclList(self):

        localctx = MiniGoParser.FieldDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fieldDeclList)
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.nonNullFieldDeclList(0)
                pass
            elif token in [MiniGoParser.R_BRACE]:
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


    class NonNullFieldDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclContext,0)


        def nonNullFieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullFieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullFieldDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullFieldDeclList" ):
                return visitor.visitNonNullFieldDeclList(self)
            else:
                return visitor.visitChildren(self)



    def nonNullFieldDeclList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.NonNullFieldDeclListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_nonNullFieldDeclList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.fieldDecl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NonNullFieldDeclListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_nonNullFieldDeclList)
                    self.state = 318
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 319
                    self.fieldDecl() 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = MiniGoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 326
            self.type_()
            self.state = 327
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDecl" ):
                return visitor.visitInterfaceDecl(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDecl(self):

        localctx = MiniGoParser.InterfaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interfaceDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.TYPE)
            self.state = 330
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 331
            self.match(MiniGoParser.INTERFACE)
            self.state = 332
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def methodDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclListContext,0)


        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = MiniGoParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_interfaceBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.L_BRACE)
            self.state = 335
            self.methodDeclList()
            self.state = 336
            self.match(MiniGoParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullMethodDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullMethodDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclList" ):
                return visitor.visitMethodDeclList(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclList(self):

        localctx = MiniGoParser.MethodDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_methodDeclList)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.nonNullMethodDeclList(0)
                pass
            elif token in [MiniGoParser.R_BRACE]:
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


    class NonNullMethodDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def nonNullMethodDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullMethodDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullMethodDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullMethodDeclList" ):
                return visitor.visitNonNullMethodDeclList(self)
            else:
                return visitor.visitChildren(self)



    def nonNullMethodDeclList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.NonNullMethodDeclListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_nonNullMethodDeclList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.methodDecl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NonNullMethodDeclListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_nonNullMethodDeclList)
                    self.state = 345
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 346
                    self.methodDecl() 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 353
            self.signature()
            self.state = 354
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtBody(self):
            return self.getTypedRuleContext(MiniGoParser.StmtBodyContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.stmtBody()
            self.state = 357
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBody" ):
                return visitor.visitStmtBody(self)
            else:
                return visitor.visitChildren(self)




    def stmtBody(self):

        localctx = MiniGoParser.StmtBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmtBody)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.constDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 364
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 365
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 366
                self.callStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 367
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOpContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MiniGoParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.lhs(0)
            self.state = 371
            self.assignOp()
            self.state = 372
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(MiniGoParser.FieldAccessContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MiniGoParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 381
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 377
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 378
                        self.fieldAccess()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 379
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 380
                        self.arrayAccess()
                        pass

             
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(MiniGoParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(MiniGoParser.SLASH_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOp" ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = MiniGoParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLON_ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.STAR_ASSIGN) | (1 << MiniGoParser.SLASH_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def ifCondition(self):
            return self.getTypedRuleContext(MiniGoParser.IfConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniGoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.IF)
            self.state = 391
            self.ifCondition()
            self.state = 392
            self.block()
            self.state = 393
            self.elseStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCondition" ):
                return visitor.visitIfCondition(self)
            else:
                return visitor.visitChildren(self)




    def ifCondition(self):

        localctx = MiniGoParser.IfConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_ifCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(MiniGoParser.L_PAREN)
            self.state = 396
            self.expression(0)
            self.state = 397
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = MiniGoParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseStmt)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(MiniGoParser.ELSE)
                self.state = 400
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(MiniGoParser.ELSE)
                self.state = 402
                self.ifStmt()
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


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopContext,0)


        def forRange(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniGoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.FOR)
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 407
                self.forCondition()
                pass

            elif la_ == 2:
                self.state = 408
                self.forLoop()
                pass

            elif la_ == 3:
                self.state = 409
                self.forRange()
                pass


            self.state = 412
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoopInit(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopInitContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def forLoopUpdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopUpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MiniGoParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.forLoopInit()
            self.state = 417
            self.match(MiniGoParser.SEMICOLON)
            self.state = 418
            self.forCondition()
            self.state = 419
            self.match(MiniGoParser.SEMICOLON)
            self.state = 420
            self.forLoopUpdate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoopUpdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopUpdateContext,0)


        def varDeclWithInit(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclWithInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoopInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoopInit" ):
                return visitor.visitForLoopInit(self)
            else:
                return visitor.visitChildren(self)




    def forLoopInit(self):

        localctx = MiniGoParser.ForLoopInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_forLoopInit)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.forLoopUpdate()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.varDeclWithInit()
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


    class ForLoopUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assignOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoopUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoopUpdate" ):
                return visitor.visitForLoopUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forLoopUpdate(self):

        localctx = MiniGoParser.ForLoopUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forLoopUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 427
            self.assignOp()
            self.state = 428
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forIndex(self):
            return self.getTypedRuleContext(MiniGoParser.ForIndexContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def forValue(self):
            return self.getTypedRuleContext(MiniGoParser.ForValueContext,0)


        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def rangeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.RangeExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.forIndex()
            self.state = 431
            self.match(MiniGoParser.COMMA)
            self.state = 432
            self.forValue()
            self.state = 433
            self.match(MiniGoParser.COLON_ASSIGN)
            self.state = 434
            self.rangeExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forIndex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIndex" ):
                return visitor.visitForIndex(self)
            else:
                return visitor.visitChildren(self)




    def forIndex(self):

        localctx = MiniGoParser.ForIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_forIndex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForValue" ):
                return visitor.visitForValue(self)
            else:
                return visitor.visitChildren(self)




    def forValue(self):

        localctx = MiniGoParser.ForValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeExpr" ):
                return visitor.visitRangeExpr(self)
            else:
                return visitor.visitChildren(self)




    def rangeExpr(self):

        localctx = MiniGoParser.RangeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_rangeExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(MiniGoParser.RANGE)
            self.state = 441
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MiniGoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = MiniGoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = MiniGoParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_callStmt)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 448
                self.arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.primaryExpr(0)
                self.state = 450
                self.match(MiniGoParser.DOT)
                self.state = 451
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 452
                self.arguments()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniGoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_returnStmt)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(MiniGoParser.RETURN)
                self.state = 457
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.match(MiniGoParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLit(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLitContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.basicLit()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.arrayLit()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.structLit()
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


    class BasicLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerLit(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerLitContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basicLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLit" ):
                return visitor.visitBasicLit(self)
            else:
                return visitor.visitChildren(self)




    def basicLit(self):

        localctx = MiniGoParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_basicLit)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.integerLit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 468
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 469
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 470
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.match(MiniGoParser.NIL)
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


    class IntegerLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_INT(self):
            return self.getToken(MiniGoParser.DECIMAL_INT, 0)

        def BINARY_INT(self):
            return self.getToken(MiniGoParser.BINARY_INT, 0)

        def OCTAL_INT(self):
            return self.getToken(MiniGoParser.OCTAL_INT, 0)

        def HEX_INT(self):
            return self.getToken(MiniGoParser.HEX_INT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_integerLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLit" ):
                return visitor.visitIntegerLit(self)
            else:
                return visitor.visitChildren(self)




    def integerLit(self):

        localctx = MiniGoParser.IntegerLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_integerLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECIMAL_INT) | (1 << MiniGoParser.BINARY_INT) | (1 << MiniGoParser.OCTAL_INT) | (1 << MiniGoParser.HEX_INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.arrayType()
            self.state = 477
            self.arrayValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def arrayTypeIndex(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeIndexContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def basicTypeAndStruct(self):
            return self.getTypedRuleContext(MiniGoParser.BasicTypeAndStructContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arrayType)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(MiniGoParser.L_BRACKET)
                self.state = 480
                self.arrayTypeIndex()
                self.state = 481
                self.match(MiniGoParser.R_BRACKET)
                self.state = 482
                self.arrayType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.match(MiniGoParser.L_BRACKET)
                self.state = 485
                self.arrayTypeIndex()
                self.state = 486
                self.match(MiniGoParser.R_BRACKET)
                self.state = 487
                self.basicTypeAndStruct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerLit(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerLitContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayTypeIndex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayTypeIndex" ):
                return visitor.visitArrayTypeIndex(self)
            else:
                return visitor.visitChildren(self)




    def arrayTypeIndex(self):

        localctx = MiniGoParser.ArrayTypeIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_arrayTypeIndex)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.integerLit()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.match(MiniGoParser.IDENTIFIER)
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


    class ArrayElementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicTypeAndStruct(self):
            return self.getTypedRuleContext(MiniGoParser.BasicTypeAndStructContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayElementType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElementType" ):
                return visitor.visitArrayElementType(self)
            else:
                return visitor.visitChildren(self)




    def arrayElementType(self):

        localctx = MiniGoParser.ArrayElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_arrayElementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.basicTypeAndStruct()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def arrayList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayListContext,0)


        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = MiniGoParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(MiniGoParser.L_BRACE)
            self.state = 498
            self.arrayList()
            self.state = 499
            self.match(MiniGoParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullArrayList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullArrayListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayList" ):
                return visitor.visitArrayList(self)
            else:
                return visitor.visitChildren(self)




    def arrayList(self):

        localctx = MiniGoParser.ArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_arrayList)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.L_BRACE, MiniGoParser.IDENTIFIER, MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.nonNullArrayList()
                pass
            elif token in [MiniGoParser.R_BRACE]:
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


    class NonNullArrayListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayElement(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nonNullArrayList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullArrayListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullArrayList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullArrayList" ):
                return visitor.visitNonNullArrayList(self)
            else:
                return visitor.visitChildren(self)




    def nonNullArrayList(self):

        localctx = MiniGoParser.NonNullArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_nonNullArrayList)
        try:
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.arrayElement()
                self.state = 506
                self.match(MiniGoParser.COMMA)
                self.state = 507
                self.nonNullArrayList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.arrayElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def basicLit(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = MiniGoParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_arrayElement)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.basicLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.structLit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.arrayValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def structValue(self):
            return self.getTypedRuleContext(MiniGoParser.StructValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.structType()
            self.state = 519
            self.structValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(MiniGoParser.L_BRACE, 0)

        def keyedElementList(self):
            return self.getTypedRuleContext(MiniGoParser.KeyedElementListContext,0)


        def R_BRACE(self):
            return self.getToken(MiniGoParser.R_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructValue" ):
                return visitor.visitStructValue(self)
            else:
                return visitor.visitChildren(self)




    def structValue(self):

        localctx = MiniGoParser.StructValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_structValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.L_BRACE)
            self.state = 524
            self.keyedElementList()
            self.state = 525
            self.match(MiniGoParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyedElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullKeyedElementList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullKeyedElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyedElementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyedElementList" ):
                return visitor.visitKeyedElementList(self)
            else:
                return visitor.visitChildren(self)




    def keyedElementList(self):

        localctx = MiniGoParser.KeyedElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_keyedElementList)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.nonNullKeyedElementList()
                pass
            elif token in [MiniGoParser.R_BRACE]:
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


    class NonNullKeyedElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyedElement(self):
            return self.getTypedRuleContext(MiniGoParser.KeyedElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nonNullKeyedElementList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullKeyedElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullKeyedElementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullKeyedElementList" ):
                return visitor.visitNonNullKeyedElementList(self)
            else:
                return visitor.visitChildren(self)




    def nonNullKeyedElementList(self):

        localctx = MiniGoParser.NonNullKeyedElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_nonNullKeyedElementList)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.keyedElement()
                self.state = 532
                self.match(MiniGoParser.COMMA)
                self.state = 533
                self.nonNullKeyedElementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.keyedElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(MiniGoParser.KeyContext,0)


        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyedElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyedElement" ):
                return visitor.visitKeyedElement(self)
            else:
                return visitor.visitChildren(self)




    def keyedElement(self):

        localctx = MiniGoParser.KeyedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_keyedElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.key()
            self.state = 539
            self.match(MiniGoParser.COLON)
            self.state = 540
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_key

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = MiniGoParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogAndExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.logAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 549
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 550
                    self.match(MiniGoParser.OR)
                    self.state = 551
                    self.logAndExpr(0) 
                self.state = 556
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self):
            return self.getTypedRuleContext(MiniGoParser.RelExprContext,0)


        def logAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogAndExprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logAndExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogAndExpr" ):
                return visitor.visitLogAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def logAndExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogAndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_logAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.relExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logAndExpr)
                    self.state = 560
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 561
                    self.match(MiniGoParser.AND)
                    self.state = 562
                    self.relExpr(0) 
                self.state = 567
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.relOp = None # Token

        def addExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AddExprContext,0)


        def relExpr(self):
            return self.getTypedRuleContext(MiniGoParser.RelExprContext,0)


        def EQUALS(self):
            return self.getToken(MiniGoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MiniGoParser.NOT_EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)



    def relExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.RelExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 152
        self.enterRecursionRule(localctx, 152, self.RULE_relExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.RelExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relExpr)
                    self.state = 571
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 572
                    localctx.relOp = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALS) | (1 << MiniGoParser.NOT_EQUALS) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_THAN_OR_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_THAN_OR_EQUAL))) != 0)):
                        localctx.relOp = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 573
                    self.addExpr(0) 
                self.state = 578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.addOp = None # Token

        def mulExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MulExprContext,0)


        def addExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AddExprContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_addExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 154
        self.enterRecursionRule(localctx, 154, self.RULE_addExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 587
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AddExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 582
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 583
                    localctx.addOp = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        localctx.addOp = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 584
                    self.mulExpr(0) 
                self.state = 589
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.mulOp = None # Token

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def mulExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MulExprContext,0)


        def STAR(self):
            return self.getToken(MiniGoParser.STAR, 0)

        def SLASH(self):
            return self.getToken(MiniGoParser.SLASH, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mulExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 156
        self.enterRecursionRule(localctx, 156, self.RULE_mulExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 598
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MulExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 593
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 594
                    localctx.mulOp = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STAR) | (1 << MiniGoParser.SLASH) | (1 << MiniGoParser.MOD))) != 0)):
                        localctx.mulOp = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 595
                    self.unaryExpr() 
                self.state = 600
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.unaryOp = None # Token

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniGoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PLUS, MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                localctx.unaryOp = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUS) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT))) != 0)):
                    localctx.unaryOp = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 602
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.primaryExpr(0)
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(MiniGoParser.FieldAccessContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayAccessContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 160
        self.enterRecursionRule(localctx, 160, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 619
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 617
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 609
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 610
                        self.fieldAccess()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 611
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 612
                        self.arrayAccess()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 613
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 614
                        self.match(MiniGoParser.DOT)
                        self.state = 615
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 616
                        self.arguments()
                        pass

             
                self.state = 621
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccess" ):
                return visitor.visitFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldAccess(self):

        localctx = MiniGoParser.FieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_fieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(MiniGoParser.DOT)
            self.state = 623
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = MiniGoParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.match(MiniGoParser.L_BRACKET)
            self.state = 626
            self.expression(0)
            self.state = 627
            self.match(MiniGoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(MiniGoParser.L_PAREN)
            self.state = 630
            self.argumentList()
            self.state = 631
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNullArgumentList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullArgumentListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniGoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_argumentList)
        try:
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.PLUS, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.L_PAREN, MiniGoParser.L_BRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.DECIMAL_INT, MiniGoParser.BINARY_INT, MiniGoParser.OCTAL_INT, MiniGoParser.HEX_INT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.nonNullArgumentList()
                pass
            elif token in [MiniGoParser.R_PAREN]:
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


    class NonNullArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nonNullArgumentList(self):
            return self.getTypedRuleContext(MiniGoParser.NonNullArgumentListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nonNullArgumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNullArgumentList" ):
                return visitor.visitNonNullArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def nonNullArgumentList(self):

        localctx = MiniGoParser.NonNullArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_nonNullArgumentList)
        try:
            self.state = 642
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                self.expression(0)
                self.state = 638
                self.match(MiniGoParser.COMMA)
                self.state = 639
                self.nonNullArgumentList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_operand)
        try:
            self.state = 652
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 646
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 647
                self.arguments()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 648
                self.match(MiniGoParser.L_PAREN)
                self.state = 649
                self.expression(0)
                self.state = 650
                self.match(MiniGoParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.declList_sempred
        self._predicates[16] = self.identifierList_sempred
        self._predicates[19] = self.nonNullStmtList_sempred
        self._predicates[26] = self.nonNullFieldDeclList_sempred
        self._predicates[31] = self.nonNullMethodDeclList_sempred
        self._predicates[36] = self.lhs_sempred
        self._predicates[74] = self.expression_sempred
        self._predicates[75] = self.logAndExpr_sempred
        self._predicates[76] = self.relExpr_sempred
        self._predicates[77] = self.addExpr_sempred
        self._predicates[78] = self.mulExpr_sempred
        self._predicates[80] = self.primaryExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def declList_sempred(self, localctx:DeclListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def identifierList_sempred(self, localctx:IdentifierListContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def nonNullStmtList_sempred(self, localctx:NonNullStmtListContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def nonNullFieldDeclList_sempred(self, localctx:NonNullFieldDeclListContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def nonNullMethodDeclList_sempred(self, localctx:NonNullMethodDeclListContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def logAndExpr_sempred(self, localctx:LogAndExprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def relExpr_sempred(self, localctx:RelExprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         




