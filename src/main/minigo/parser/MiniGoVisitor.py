# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declList.
    def visitDeclList(self, ctx:MiniGoParser.DeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declBody.
    def visitDeclBody(self, ctx:MiniGoParser.DeclBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclWithInit.
    def visitVarDeclWithInit(self, ctx:MiniGoParser.VarDeclWithInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_.
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicTypeAndStruct.
    def visitBasicTypeAndStruct(self, ctx:MiniGoParser.BasicTypeAndStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initilization.
    def visitInitilization(self, ctx:MiniGoParser.InitilizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#signature.
    def visitSignature(self, ctx:MiniGoParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterList.
    def visitParameterList(self, ctx:MiniGoParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnType.
    def visitReturnType(self, ctx:MiniGoParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterDeclList.
    def visitParameterDeclList(self, ctx:MiniGoParser.ParameterDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullParameterDeclList.
    def visitNonNullParameterDeclList(self, ctx:MiniGoParser.NonNullParameterDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtList.
    def visitStmtList(self, ctx:MiniGoParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullStmtList.
    def visitNonNullStmtList(self, ctx:MiniGoParser.NonNullStmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDefine.
    def visitMethodDefine(self, ctx:MiniGoParser.MethodDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiverType.
    def visitReceiverType(self, ctx:MiniGoParser.ReceiverTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDecl.
    def visitStructDecl(self, ctx:MiniGoParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structBody.
    def visitStructBody(self, ctx:MiniGoParser.StructBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDeclList.
    def visitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullFieldDeclList.
    def visitNonNullFieldDeclList(self, ctx:MiniGoParser.NonNullFieldDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDecl.
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:MiniGoParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceBody.
    def visitInterfaceBody(self, ctx:MiniGoParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDeclList.
    def visitMethodDeclList(self, ctx:MiniGoParser.MethodDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullMethodDeclList.
    def visitNonNullMethodDeclList(self, ctx:MiniGoParser.NonNullMethodDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtBody.
    def visitStmtBody(self, ctx:MiniGoParser.StmtBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniGoParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignOp.
    def visitAssignOp(self, ctx:MiniGoParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStmt.
    def visitIfStmt(self, ctx:MiniGoParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifCondition.
    def visitIfCondition(self, ctx:MiniGoParser.IfConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseStmt.
    def visitElseStmt(self, ctx:MiniGoParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStmt.
    def visitForStmt(self, ctx:MiniGoParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forLoop.
    def visitForLoop(self, ctx:MiniGoParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forLoopInit.
    def visitForLoopInit(self, ctx:MiniGoParser.ForLoopInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forLoopUpdate.
    def visitForLoopUpdate(self, ctx:MiniGoParser.ForLoopUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRange.
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forIndex.
    def visitForIndex(self, ctx:MiniGoParser.ForIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forValue.
    def visitForValue(self, ctx:MiniGoParser.ForValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rangeExpr.
    def visitRangeExpr(self, ctx:MiniGoParser.RangeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniGoParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStmt.
    def visitContinueStmt(self, ctx:MiniGoParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStmt.
    def visitCallStmt(self, ctx:MiniGoParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniGoParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicLit.
    def visitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#integerLit.
    def visitIntegerLit(self, ctx:MiniGoParser.IntegerLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayTypeIndex.
    def visitArrayTypeIndex(self, ctx:MiniGoParser.ArrayTypeIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayElementType.
    def visitArrayElementType(self, ctx:MiniGoParser.ArrayElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayValue.
    def visitArrayValue(self, ctx:MiniGoParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayList.
    def visitArrayList(self, ctx:MiniGoParser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullArrayList.
    def visitNonNullArrayList(self, ctx:MiniGoParser.NonNullArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayElement.
    def visitArrayElement(self, ctx:MiniGoParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structValue.
    def visitStructValue(self, ctx:MiniGoParser.StructValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyedElementList.
    def visitKeyedElementList(self, ctx:MiniGoParser.KeyedElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullKeyedElementList.
    def visitNonNullKeyedElementList(self, ctx:MiniGoParser.NonNullKeyedElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyedElement.
    def visitKeyedElement(self, ctx:MiniGoParser.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#key.
    def visitKey(self, ctx:MiniGoParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logAndExpr.
    def visitLogAndExpr(self, ctx:MiniGoParser.LogAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relExpr.
    def visitRelExpr(self, ctx:MiniGoParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#addExpr.
    def visitAddExpr(self, ctx:MiniGoParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mulExpr.
    def visitMulExpr(self, ctx:MiniGoParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldAccess.
    def visitFieldAccess(self, ctx:MiniGoParser.FieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniGoParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentList.
    def visitArgumentList(self, ctx:MiniGoParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nonNullArgumentList.
    def visitNonNullArgumentList(self, ctx:MiniGoParser.NonNullArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)



del MiniGoParser