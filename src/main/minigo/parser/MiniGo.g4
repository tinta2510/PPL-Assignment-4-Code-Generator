// Student ID: 2213506
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

// Lexer rules
NL: ('\r'?'\n') {
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
}; 

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs

LINE_COMMENT: '//' ~[\r\n]* -> skip;

MULTI_LINE_COMMENT: '/*' ( MULTI_LINE_COMMENT | .)*? '*/' -> skip; 

// Keywords
IF: 'if';

ELSE: 'else';

FOR: 'for';

RETURN: 'return';

FUNC: 'func';

TYPE: 'type';

STRUCT: 'struct';

INTERFACE: 'interface';

STRING: 'string';

INT: 'int';

FLOAT: 'float';

BOOLEAN: 'boolean';

CONST: 'const';

VAR: 'var';

CONTINUE: 'continue';

BREAK: 'break';

RANGE: 'range';

NIL: 'nil';

TRUE: 'true';

FALSE: 'false';

// Operators
PLUS: '+';

MINUS: '-';

STAR: '*';

SLASH: '/';

MOD: '%';

EQUALS: '==';

NOT_EQUALS: '!=';

LESS_THAN: '<';

LESS_THAN_OR_EQUAL: '<=';

GREATER_THAN: '>';

GREATER_THAN_OR_EQUAL: '>=';

AND: '&&';

OR: '||';

NOT: '!';

ASSIGN: '=';

COLON_ASSIGN: ':=';

PLUS_ASSIGN: '+=';

MINUS_ASSIGN: '-=';

STAR_ASSIGN: '*=';

SLASH_ASSIGN: '/=';

MOD_ASSIGN: '%=';

DOT: '.';

COLON: ':';

// Separators
L_PAREN: '(';

R_PAREN: ')';

L_BRACE: '{';

R_BRACE: '}';

L_BRACKET: '[';

R_BRACKET: ']';

COMMA: ',';

SEMICOLON: ';';

// Identifiers (go after keywords)
IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;

// INT Literals
DECIMAL_INT: [1-9]DIGIT* | '0'; 
fragment DIGIT: [0-9];
BINARY_INT: '0'[Bb][01]+ ; 
OCTAL_INT: '0'[Oo][0-7]+ ;
HEX_INT: '0'[Xx][0-9A-Fa-f]+ ;

FLOAT_LIT: DIGIT+ '.' DIGIT* EXPONENT?; 

fragment EXPONENT: [eE][+-]? DIGIT+;

STRING_LIT: '"' STRING_CHAR* '"' ; 

fragment STRING_CHAR: (~[\n"\\] | '\\' [ntr"\\]);

ERROR_CHAR: . ;

ILLEGAL_ESCAPE: '"' STRING_CHAR* '\\' ~[ntr"\\] ;

UNCLOSE_STRING: '"' STRING_CHAR* ('\r'? '\n' | EOF) {
    if (self.text[-1] == '\n' and self.text[-2] == '\r'):
        self.text = self.text[:-2];
    elif (self.text[-1] == '\n'):
        self.text = self.text[:-1];
    else:
        self.text = self.text[:]
}; 

// Parser rules
program  : declList EOF ;

// Declaration
declList: decl | declList decl ;

decl: declBody eos ;

declBody: varDecl | constDecl | funcDecl | methodDefine | structDecl | interfaceDecl ;

varDecl
    : varDeclWithInit
    | VAR IDENTIFIER type_
    ;

varDeclWithInit
    : VAR IDENTIFIER type_ initilization 
    | VAR IDENTIFIER initilization
    ;

type_: basicTypeAndStruct | arrayType ;

basicTypeAndStruct: IDENTIFIER | STRING | INT | FLOAT | BOOLEAN ;

initilization: ASSIGN expression ;

constDecl: CONST IDENTIFIER initilization ;

funcDecl: FUNC IDENTIFIER signature block ;

signature
    : parameterList returnType
    | parameterList ;

parameterList: L_PAREN parameterDeclList R_PAREN ;

returnType: type_;

parameterDeclList: nonNullParameterDeclList | ; // nullable

nonNullParameterDeclList: identifierList type_ COMMA nonNullParameterDeclList | identifierList type_ ;

identifierList: IDENTIFIER | identifierList COMMA IDENTIFIER ;

block: L_BRACE stmtList R_BRACE ; 

stmtList: nonNullStmtList | ; //nullable

nonNullStmtList: stmt | nonNullStmtList stmt ;

methodDefine: FUNC receiver IDENTIFIER signature block ;

receiver: L_PAREN IDENTIFIER receiverType R_PAREN ;

receiverType: IDENTIFIER ;

structDecl: TYPE IDENTIFIER STRUCT structBody ;

structBody: L_BRACE fieldDeclList R_BRACE ;

fieldDeclList: nonNullFieldDeclList | ;

nonNullFieldDeclList: fieldDecl | nonNullFieldDeclList fieldDecl ;

fieldDecl: IDENTIFIER type_ eos ;

interfaceDecl: TYPE IDENTIFIER INTERFACE interfaceBody;

interfaceBody: L_BRACE methodDeclList R_BRACE ;

methodDeclList: nonNullMethodDeclList | ;

nonNullMethodDeclList: methodDecl | nonNullMethodDeclList methodDecl ;

methodDecl: IDENTIFIER signature eos;

// Statement
stmt: stmtBody eos ;

stmtBody
    : varDecl | constDecl | assignStmt | ifStmt | forStmt | breakStmt 
    | continueStmt | callStmt | returnStmt ;

assignStmt: lhs assignOp rhs ;

lhs: IDENTIFIER | lhs fieldAccess | lhs arrayAccess ; 

assignOp: COLON_ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | MOD_ASSIGN ;

rhs: expression ;

ifStmt: IF ifCondition block elseStmt ;

ifCondition: L_PAREN expression R_PAREN ;

elseStmt: ELSE block | ELSE ifStmt | ;

forStmt: FOR ( forCondition | forLoop | forRange ) block ;

forCondition: expression ;

forLoop: forLoopInit SEMICOLON forCondition SEMICOLON forLoopUpdate ;

forLoopInit: forLoopUpdate | varDeclWithInit ;

forLoopUpdate: IDENTIFIER assignOp expression ;

forRange: forIndex COMMA forValue COLON_ASSIGN rangeExpr ;

forIndex: IDENTIFIER ;

forValue: IDENTIFIER ;

rangeExpr: RANGE expression ; 

breakStmt: BREAK ;

continueStmt: CONTINUE ;

callStmt: IDENTIFIER arguments | primaryExpr DOT IDENTIFIER arguments ; //???lhs

returnStmt: RETURN expression | RETURN ;

// Expression
literal: basicLit | arrayLit | structLit  ;

basicLit: integerLit | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL ;

integerLit: DECIMAL_INT | BINARY_INT | OCTAL_INT | HEX_INT ;

arrayLit: arrayType arrayValue ;

arrayType
    : L_BRACKET arrayTypeIndex R_BRACKET arrayType 
    | L_BRACKET arrayTypeIndex R_BRACKET basicTypeAndStruct; 

arrayTypeIndex: integerLit | IDENTIFIER ;

arrayElementType: basicTypeAndStruct ;

arrayValue: L_BRACE arrayList R_BRACE;

arrayList: nonNullArrayList | ; //???: nullable

nonNullArrayList: arrayElement COMMA nonNullArrayList | arrayElement ;

arrayElement: IDENTIFIER | basicLit | structLit | arrayValue ; 

structLit: structType structValue ;

structType: IDENTIFIER ;

structValue: L_BRACE keyedElementList R_BRACE; 

keyedElementList: nonNullKeyedElementList | ; 

nonNullKeyedElementList: keyedElement COMMA nonNullKeyedElementList | keyedElement ;

keyedElement: key COLON element ;

key: IDENTIFIER ; 

element: expression ; 

expression: expression OR logAndExpr |  logAndExpr ;

logAndExpr: logAndExpr AND relExpr | relExpr ;

relExpr: relExpr relOp = ( EQUALS | NOT_EQUALS | LESS_THAN | LESS_THAN_OR_EQUAL 
    | GREATER_THAN | GREATER_THAN_OR_EQUAL ) addExpr | addExpr ;

addExpr: addExpr addOp = (PLUS | MINUS) mulExpr | mulExpr ;

mulExpr: mulExpr mulOp = (STAR | SLASH | MOD) unaryExpr | unaryExpr ;

unaryExpr: unaryOp = (PLUS | MINUS | NOT) unaryExpr | primaryExpr ;

primaryExpr
    : operand                               
    | primaryExpr fieldAccess               
    | primaryExpr arrayAccess               
    | primaryExpr DOT IDENTIFIER arguments  //methodCall
    ; 

fieldAccess: DOT IDENTIFIER ;

arrayAccess: L_BRACKET expression R_BRACKET ;

arguments: L_PAREN argumentList R_PAREN ;

argumentList: nonNullArgumentList | ;

nonNullArgumentList: expression COMMA nonNullArgumentList | expression ;

operand
    : literal 
    | IDENTIFIER 
    | IDENTIFIER arguments 
    | L_PAREN expression R_PAREN 
    ; 

eos: SEMICOLON | NL;