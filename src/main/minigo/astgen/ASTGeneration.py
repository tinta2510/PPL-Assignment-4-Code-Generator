from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):

    # program  : declList EOF ;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.declList()))

    # declList: decl | declList decl;
    def visitDeclList(self, ctx:MiniGoParser.DeclListContext):
        return (
            (self.visit(ctx.declList()) if ctx.declList() else []) + 
            [self.visit(ctx.decl())]
        )

    # decl: declBody eos ;
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.declBody())

    # declBody: varDecl | constDecl | funcDecl | methodDefine | structDecl | interfaceDecl ;
    def visitDeclBody(self, ctx:MiniGoParser.DeclBodyContext):
        return self.visit(ctx.getChild(0))

    # varDecl: varDeclWithInit | VAR IDENTIFIER type_ ;
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        if ctx.varDeclWithInit():
            return self.visit(ctx.varDeclWithInit())
        else:
            return VarDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.type_()), None)

    # varDeclWithInit: VAR IDENTIFIER type_ initilization | VAR IDENTIFIER initilization;
    def visitVarDeclWithInit(self, ctx:MiniGoParser.VarDeclWithInitContext):
        return VarDecl(ctx.IDENTIFIER().getText(), 
                        self.visit(ctx.type_()) if ctx.type_() else None, 
                        self.visit(ctx.initilization())
                        )

    # type_: basicTypeAndStruct | arrayType ;
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        if ctx.basicTypeAndStruct():
            return self.visit(ctx.basicTypeAndStruct())
        elif ctx.arrayType():
            dimensions, elementType = self.visit(ctx.arrayType())
            return ArrayType(dimensions, elementType)
        
    # basicTypeAndStruct: IDENTIFIER | STRING | INT | FLOAT | BOOLEAN ;
    def visitBasicTypeAndStruct(self, ctx:MiniGoParser.BasicTypeAndStructContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText()) 
        elif ctx.STRING():
            return StringType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()

    # initilization: ASSIGN expression ;
    def visitInitilization(self, ctx:MiniGoParser.InitilizationContext):
        return self.visit(ctx.expression())

    # constDecl: CONST IDENTIFIER initilization ;
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return ConstDecl(ctx.IDENTIFIER().getText(), None, self.visit(ctx.initilization()))

    # funcDecl: FUNC IDENTIFIER signature block ;
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        params, returnType = self.visit(ctx.signature())
        return FuncDecl(
            ctx.IDENTIFIER().getText(), 
            params, 
            returnType,
            self.visit(ctx.block())
        )

    # signature: parameterList returnType | parameterList ;
    def visitSignature(self, ctx:MiniGoParser.SignatureContext):
        return self.visit(ctx.parameterList()), self.visit(ctx.returnType()) if ctx.returnType() else VoidType()

    # parameterList: L_PAREN parameterDeclList R_PAREN ;
    def visitParameterList(self, ctx:MiniGoParser.ParameterListContext):
        return self.visit(ctx.parameterDeclList())

    # returnType: type_;
    def visitReturnType(self, ctx:MiniGoParser.ReturnTypeContext):
        return self.visit(ctx.type_())

    # parameterDeclList: nonNullParameterDeclList | ;
    def visitParameterDeclList(self, ctx:MiniGoParser.ParameterDeclListContext):
        if ctx.nonNullParameterDeclList():
            return self.visit(ctx.nonNullParameterDeclList())
        else:
            return []

    # nonNullParameterDeclList: identifierList type_ COMMA nonNullParameterDeclList | identifierList type_ ;
    def visitNonNullParameterDeclList(self, ctx:MiniGoParser.NonNullParameterDeclListContext):
        identifier_list = self.visit(ctx.identifierList())
        type_ = self.visit(ctx.type_())
        var_decl_list = [ParamDecl(identifier, type_) for identifier in identifier_list]
        return (
            var_decl_list + 
            (self.visit(ctx.nonNullParameterDeclList()) if ctx.nonNullParameterDeclList() else [])
        )

    # identifierList: IDENTIFIER | identifierList COMMA IDENTIFIER ;
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return (
            (self.visit(ctx.identifierList()) if ctx.identifierList() else []) +
            [ctx.IDENTIFIER().getText()] 
        )

    # block: L_BRACE stmtList R_BRACE ; 
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return Block(self.visit(ctx.stmtList())) 
    
    # stmtList: nonNullStmtList | ;
    def visitStmtList(self, ctx:MiniGoParser.StmtListContext):
        if ctx.nonNullStmtList():
            return self.visit(ctx.nonNullStmtList())
        else:
            return []

    # nonNullStmtList: stmt | nonNullStmtList stmt ;
    def visitNonNullStmtList(self, ctx:MiniGoParser.NonNullStmtListContext):
        if ctx.nonNullStmtList():
            return self.visit(ctx.nonNullStmtList()) + [self.visit(ctx.stmt())]
        else:
            return [self.visit(ctx.stmt())]

    # methodDefine: FUNC receiver IDENTIFIER signature block ;
    def visitMethodDefine(self, ctx:MiniGoParser.MethodDefineContext):
        params, returnType = self.visit(ctx.signature())
        receiverName, receiverType = self.visit(ctx.receiver())
        return MethodDecl(
            receiverName, # receiver
            receiverType, # recType
            FuncDecl(
                ctx.IDENTIFIER().getText(), 
                params, 
                returnType,
                self.visit(ctx.block())
            )
        )

    # receiver: L_PAREN IDENTIFIER receiverType R_PAREN ;
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        '''Result: (receiverName, receiverType)'''
        return ctx.IDENTIFIER().getText(), self.visit(ctx.receiverType())

    # receiverType: IDENTIFIER ;
    def visitReceiverType(self, ctx:MiniGoParser.ReceiverTypeContext):
        return Id(ctx.IDENTIFIER().getText())

    # structDecl: TYPE IDENTIFIER STRUCT structBody ;
    def visitStructDecl(self, ctx:MiniGoParser.StructDeclContext):
        return StructType(
            ctx.IDENTIFIER().getText(), 
            self.visit(ctx.structBody()), 
            []
        )

    # structBody: L_BRACE fieldDeclList R_BRACE ;
    def visitStructBody(self, ctx:MiniGoParser.StructBodyContext):
        return self.visit(ctx.fieldDeclList())

    # fieldDeclList: nonNullFieldDeclList | ;
    def visitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        if ctx.nonNullFieldDeclList():
            return self.visit(ctx.nonNullFieldDeclList())
        else:
            return []

    # nonNullFieldDeclList: fieldDecl | nonNullFieldDeclList fieldDecl ;
    def visitNonNullFieldDeclList(self, ctx:MiniGoParser.NonNullFieldDeclListContext):
        if ctx.nonNullFieldDeclList():
            return self.visit(ctx.nonNullFieldDeclList()) + [self.visit(ctx.fieldDecl())]
        else:
            return [self.visit(ctx.fieldDecl())]

    # fieldDecl: IDENTIFIER type_ eos ;
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        return (ctx.IDENTIFIER().getText(), self.visit(ctx.type_()))

    # interfaceDecl: TYPE IDENTIFIER INTERFACE interfaceBody;
    def visitInterfaceDecl(self, ctx:MiniGoParser.InterfaceDeclContext):
        return InterfaceType(ctx.IDENTIFIER().getText(), self.visit(ctx.interfaceBody()))

    # interfaceBody: L_BRACE methodDeclList R_BRACE ;
    def visitInterfaceBody(self, ctx:MiniGoParser.InterfaceBodyContext):
        return self.visit(ctx.methodDeclList())

    # methodDeclList: nonNullMethodDeclList | ;
    def visitMethodDeclList(self, ctx:MiniGoParser.MethodDeclListContext):
        if ctx.nonNullMethodDeclList():
            return self.visit(ctx.nonNullMethodDeclList())
        else:
            return []

    # nonNullMethodDeclList: methodDecl | nonNullMethodDeclList methodDecl ;
    def visitNonNullMethodDeclList(self, ctx:MiniGoParser.NonNullMethodDeclListContext):
        if ctx.nonNullMethodDeclList():
            return self.visit(ctx.nonNullMethodDeclList()) + [self.visit(ctx.methodDecl())]
        else:
            return [self.visit(ctx.methodDecl())]

    # methodDecl: IDENTIFIER signature eos;
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        params, returnType = self.visit(ctx.signature()) 
        params_type_lst = [param.parType for param in params]
        return Prototype(ctx.IDENTIFIER().getText(), params_type_lst, returnType)

    # stmt: stmtBody eos ;
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visit(ctx.stmtBody())

    # stmtBody
    #     : varDecl | constDecl | assignStmt | ifStmt | forStmt | breakStmt 
    #     | continueStmt | callStmt | returnStmt ;
    def visitStmtBody(self, ctx:MiniGoParser.StmtBodyContext):
        return self.visit(ctx.getChild(0))

    # assignStmt: lhs assignOp rhs ;
    def visitAssignStmt(self, ctx:MiniGoParser.AssignStmtContext):
        assign_op = self.visit(ctx.assignOp())
        if assign_op == ':=':
            return Assign(
                self.visit(ctx.lhs()), 
                self.visit(ctx.rhs())
            )
        else:
            return Assign(
                self.visit(ctx.lhs()), 
                BinaryOp(
                    assign_op[0], 
                    self.visit(ctx.lhs()), 
                    self.visit(ctx.rhs())
                )
            )

    # lhs: IDENTIFIER | lhs fieldAccess | lhs arrayAccess ; 
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.fieldAccess():
            return FieldAccess(
                self.visit(ctx.lhs()), 
                self.visit(ctx.fieldAccess())
            )
        elif ctx.arrayAccess():
            accessed_arr = self.visit(ctx.lhs())
            if type(accessed_arr) == ArrayCell:
                arr, prev_idx = accessed_arr.arr, accessed_arr.idx
            else:
                arr, prev_idx = accessed_arr, []
            return ArrayCell(
                arr, 
                prev_idx + self.visit(ctx.arrayAccess())
            )

    # assignOp: COLON_ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | MOD_ASSIGN ;
    def visitAssignOp(self, ctx:MiniGoParser.AssignOpContext):
        return ctx.getChild(0).getText()

    # rhs: expression ;
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visit(ctx.expression())

    # ifStmt: IF ifCondition block elseStmt ;
    def visitIfStmt(self, ctx:MiniGoParser.IfStmtContext):
        return If(
            self.visit(ctx.ifCondition()),
            self.visit(ctx.block()),
            self.visit(ctx.elseStmt()) # Return None if there is no elseStmt
        )

    # ifCondition: L_PAREN expression R_PAREN ;
    def visitIfCondition(self, ctx:MiniGoParser.IfConditionContext):
        return self.visit(ctx.expression())

    # elseStmt: ELSE block | ELSE ifStmt | ;
    def visitElseStmt(self, ctx:MiniGoParser.ElseStmtContext):
        if ctx.block():
            return self.visit(ctx.block())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        else:
            return None

    # forStmt: FOR ( forCondition | forLoop | forRange ) block ;
    def visitForStmt(self, ctx:MiniGoParser.ForStmtContext):
        if ctx.forCondition():
            return ForBasic(
                self.visit(ctx.forCondition()),
                self.visit(ctx.block())
            )
        elif ctx.forLoop():
            init, condition, update = self.visit(ctx.forLoop())
            return ForStep(
                init, 
                condition, 
                update, 
                self.visit(ctx.block())
            )
        elif ctx.forRange():
            idx, value, array = self.visit(ctx.forRange())
            return ForEach(
                idx, 
                value, 
                array, 
                self.visit(ctx.block())
            )
            
    # forCondition: expression ;
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visit(ctx.expression())

    # forLoop: forLoopInit SEMICOLON forCondition SEMICOLON forLoopUpdate ;
    def visitForLoop(self, ctx:MiniGoParser.ForLoopContext):
        return (
            self.visit(ctx.forLoopInit()), # Stmt
            self.visit(ctx.forCondition()), # Expr
            self.visit(ctx.forLoopUpdate()) # Assign
        )

    # forLoopInit: forLoopUpdate | varDeclWithInit ;
    def visitForLoopInit(self, ctx:MiniGoParser.ForLoopInitContext):
        return self.visit(ctx.getChild(0)) 

    # forLoopUpdate: IDENTIFIER assignOp expression ;
    def visitForLoopUpdate(self, ctx:MiniGoParser.ForLoopUpdateContext):
        assign_op = self.visit(ctx.assignOp())
        if assign_op == ':=':
            return Assign(
                Id(ctx.IDENTIFIER().getText()), 
                self.visit(ctx.expression())
            )
        else:
            return Assign(
                Id(ctx.IDENTIFIER().getText()), 
                BinaryOp(
                    assign_op[0], 
                    Id(ctx.IDENTIFIER().getText()), 
                    self.visit(ctx.expression())
                )
            )

    # forRange: forIndex COMMA forValue COLON_ASSIGN rangeExpr ;
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return (
            self.visit(ctx.forIndex()), # Id
            self.visit(ctx.forValue()), # Id
            self.visit(ctx.rangeExpr()) # Expr
        )

    # forIndex: IDENTIFIER ;
    def visitForIndex(self, ctx:MiniGoParser.ForIndexContext):
        return Id(ctx.IDENTIFIER().getText())

    # forValue: IDENTIFIER ;
    def visitForValue(self, ctx:MiniGoParser.ForValueContext):
        return Id(ctx.IDENTIFIER().getText())

    # rangeExpr: RANGE expression ; 
    def visitRangeExpr(self, ctx:MiniGoParser.RangeExprContext):
        return self.visit(ctx.expression())

    # breakStmt: BREAK ;
    def visitBreakStmt(self, ctx:MiniGoParser.BreakStmtContext):
        return Break()

    # continueStmt: CONTINUE ;
    def visitContinueStmt(self, ctx:MiniGoParser.ContinueStmtContext):
        return Continue()

    # callStmt: IDENTIFIER arguments | primaryExpr DOT IDENTIFIER arguments ;
    def visitCallStmt(self, ctx:MiniGoParser.CallStmtContext):
        if ctx.DOT():
            return MethCall(
                self.visit(ctx.primaryExpr()), 
                ctx.IDENTIFIER().getText(), 
                self.visit(ctx.arguments())
            )
        else:
            return FuncCall(
                ctx.IDENTIFIER().getText(), 
                self.visit(ctx.arguments())
            )

    # returnStmt: RETURN expression | RETURN ;
    def visitReturnStmt(self, ctx:MiniGoParser.ReturnStmtContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)

    # literal: basicLit | arrayLit | structLit  ;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.basicLit():
            return self.visit(ctx.basicLit())
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.structLit():
            return self.visit(ctx.structLit())

    # basicLit: integerLit | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL ;
    def visitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        if ctx.integerLit():
            return self.visit(ctx.integerLit())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText()) #??? Not type casted to float
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()) #??? Not Remove open and closed quotes
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText()) #??? return "True" or "true"
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText()) #??? return "False" or "false"
        elif ctx.NIL():
            return NilLiteral()

    # integerLit: DECIMAL_INT | BINARY_INT | OCTAL_INT | HEX_INT ;
    def visitIntegerLit(self, ctx:MiniGoParser.IntegerLitContext):
        return IntLiteral(ctx.getChild(0).getText())
        
    # arrayLit: arrayType arrayValue ;
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        dimensions, elementType = self.visit(ctx.arrayType())
        return ArrayLiteral(
            dimensions,
            elementType,
            self.visit(ctx.arrayValue()) 
        )
        
    # arrayType
    #     : L_BRACKET arrayTypeIndex R_BRACKET arrayType 
    #     | L_BRACKET arrayTypeIndex R_BRACKET basicTypeAndStruct; 
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        '''Result: (dimensions, elementType)'''
        if ctx.arrayType():
            dimensions, elementType = self.visit(ctx.arrayType())
            return [self.visit(ctx.arrayTypeIndex())] + dimensions, elementType
        else:
            return [self.visit(ctx.arrayTypeIndex())], self.visit(ctx.basicTypeAndStruct())
    
    # arrayTypeIndex: integerLit | IDENTIFIER ;
    def visitArrayTypeIndex(self, ctx:MiniGoParser.ArrayTypeIndexContext):
        if ctx.integerLit():
            return self.visit(ctx.integerLit())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText()) 

    # arrayElementType: basicTypeAndStruct ;
    def visitArrayElementType(self, ctx:MiniGoParser.ArrayElementTypeContext):
        return self.visit(ctx.basicTypeAndStruct())

    # arrayValue: L_BRACE arrayList R_BRACE;
    def visitArrayValue(self, ctx:MiniGoParser.ArrayValueContext):
        return self.visit(ctx.arrayList())

    # arrayList: nonNullArrayList | ;
    def visitArrayList(self, ctx:MiniGoParser.ArrayListContext):
        if ctx.nonNullArrayList():
            return self.visit(ctx.nonNullArrayList())
        else:
            return []

    # nonNullArrayList: arrayElement COMMA nonNullArrayList | arrayElement ;
    def visitNonNullArrayList(self, ctx:MiniGoParser.NonNullArrayListContext):
        return (
            [self.visit(ctx.arrayElement())] + 
            (self.visit(ctx.nonNullArrayList()) if ctx.nonNullArrayList() else [])
        )

    # arrayElement: IDENTIFIER | basicLit | structLit | arrayValue ; 
    def visitArrayElement(self, ctx:MiniGoParser.ArrayElementContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText()) 
        elif ctx.basicLit():
            return self.visit(ctx.basicLit())
        elif ctx.structLit():
            return self.visit(ctx.structLit()) 
        elif ctx.arrayValue():
            return self.visit(ctx.arrayValue())

    # structLit: structType structValue ;
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return StructLiteral(
            self.visit(ctx.structType()), 
            self.visit(ctx.structValue())
        )

    # structType: IDENTIFIER ;
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return ctx.IDENTIFIER().getText()

    # structValue: L_BRACE keyedElementList R_BRACE; 
    def visitStructValue(self, ctx:MiniGoParser.StructValueContext):
        return self.visit(ctx.keyedElementList())

    # keyedElementList: nonNullKeyedElementList | ; 
    def visitKeyedElementList(self, ctx:MiniGoParser.KeyedElementListContext):
        if ctx.nonNullKeyedElementList():
            return self.visit(ctx.nonNullKeyedElementList())
        else:
            return []

    # nonNullKeyedElementList: keyedElement COMMA nonNullKeyedElementList | keyedElement ;
    def visitNonNullKeyedElementList(self, ctx:MiniGoParser.NonNullKeyedElementListContext):
        return (
            [self.visit(ctx.keyedElement())] + 
            (self.visit(ctx.nonNullKeyedElementList()) if ctx.nonNullKeyedElementList() else [])
        )

    # keyedElement: key COLON element ;
    def visitKeyedElement(self, ctx:MiniGoParser.KeyedElementContext):
        return (self.visit(ctx.key()), self.visit(ctx.element()))

    # key: IDENTIFIER ; 
    def visitKey(self, ctx:MiniGoParser.KeyContext):
        return ctx.IDENTIFIER().getText()

    # element: expression ; 
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visit(ctx.expression())

    # expression: expression OR logAndExpr |  logAndExpr ;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.OR():
            return BinaryOp(
                ctx.OR().getText(), 
                self.visit(ctx.expression()),
                self.visit(ctx.logAndExpr())
            )
        else:
            return self.visit(ctx.logAndExpr())

    # logAndExpr: logAndExpr AND relExpr | relExpr ;
    def visitLogAndExpr(self, ctx:MiniGoParser.LogAndExprContext):
        if ctx.AND():
            return BinaryOp(
                ctx.AND().getText(), 
                self.visit(ctx.logAndExpr()),
                self.visit(ctx.relExpr())
            )
        else:
            return self.visit(ctx.relExpr())

    # relExpr relOp = ( EQUALS | NOT_EQUALS | ...) addExpr | addExpr ;
    def visitRelExpr(self, ctx:MiniGoParser.RelExprContext):
        if ctx.getChildCount() == 3:
            rel_op = ctx.getChild(1).getText()
            return BinaryOp(
                rel_op,
                self.visit(ctx.relExpr()),
                self.visit(ctx.addExpr())
            )
        else:
            return self.visit(ctx.addExpr())

    # addExpr: addExpr addOp = (PLUS | MINUS) mulExpr | mulExpr ;
    def visitAddExpr(self, ctx:MiniGoParser.AddExprContext):
        if ctx.getChildCount() == 3:
            add_op = ctx.getChild(1).getText()
            return BinaryOp(
                add_op,
                self.visit(ctx.addExpr()),
                self.visit(ctx.mulExpr())
            )
        else:
            return self.visit(ctx.mulExpr())

    # mulExpr: mulExpr mulOp = (STAR | SLASH | MOD) unaryExpr | unaryExpr ;
    def visitMulExpr(self, ctx:MiniGoParser.MulExprContext):
        if ctx.getChildCount() == 3:
            mul_op = ctx.getChild(1).getText()
            return BinaryOp(
                mul_op,
                self.visit(ctx.mulExpr()),
                self.visit(ctx.unaryExpr())
            )
        else:
            return self.visit(ctx.unaryExpr())


    # unaryExpr: unaryOp = (PLUS | MINUS | NOT) unaryExpr | primaryExpr ;
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        if ctx.getChildCount() == 2:
            unary_op = ctx.getChild(0).getText()
            return UnaryOp(
                unary_op,
                self.visit(ctx.unaryExpr())
            )
        else:
            return self.visit(ctx.primaryExpr())

    # primaryExpr
    #     : operand
    #     | primaryExpr fieldAccess 
    #     | primaryExpr arrayAccess      
    #     | primaryExpr DOT IDENTIFIER arguments
    #     ; 
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        if ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.fieldAccess():
            return FieldAccess(
                self.visit(ctx.primaryExpr()), 
                self.visit(ctx.fieldAccess())
            )
        elif ctx.arrayAccess():
            accessed_arr = self.visit(ctx.primaryExpr())
            if type(accessed_arr) == ArrayCell:
                arr, prev_idx = accessed_arr.arr, accessed_arr.idx
            else:
                arr, prev_idx = accessed_arr, []
            return ArrayCell(
                arr, 
                prev_idx + self.visit(ctx.arrayAccess())
            )
        elif ctx.arguments() and ctx.DOT(): # method call
            return MethCall(
                self.visit(ctx.primaryExpr()), 
                ctx.IDENTIFIER().getText(), 
                self.visit(ctx.arguments())
            )

    # fieldAccess: DOT IDENTIFIER ;
    def visitFieldAccess(self, ctx:MiniGoParser.FieldAccessContext):
        return ctx.IDENTIFIER().getText()

    # arrayAccess: L_BRACKET expression R_BRACKET ;
    def visitArrayAccess(self, ctx:MiniGoParser.ArrayAccessContext):
        return [self.visit(ctx.expression())]

    # arguments: L_PAREN argumentList R_PAREN ;
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visit(ctx.argumentList())

    # argumentList: nonNullArgumentList | ;
    def visitArgumentList(self, ctx:MiniGoParser.ArgumentListContext):
        if ctx.nonNullArgumentList():
            return self.visit(ctx.nonNullArgumentList())
        else:
            return []

    # nonNullArgumentList: expression COMMA nonNullArgumentList | expression ;
    def visitNonNullArgumentList(self, ctx:MiniGoParser.NonNullArgumentListContext):
        return (
            [self.visit(ctx.expression())] + 
            (self.visit(ctx.nonNullArgumentList()) if ctx.nonNullArgumentList() else [])
        )

    # operand
    #     : literal 
    #     | IDENTIFIER 
    #     | IDENTIFIER arguments 
    #     | L_PAREN expression R_PAREN 
    #     ; 
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.arguments(): # function call
            return FuncCall(
                ctx.IDENTIFIER().getText(), 
                self.visit(ctx.arguments())
            )
        elif ctx.IDENTIFIER() and not ctx.arguments():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())

    # eos: SEMICOLON | NL;
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return None