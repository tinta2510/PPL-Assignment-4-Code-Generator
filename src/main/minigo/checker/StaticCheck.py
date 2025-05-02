"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    
    def __repr__(self):
        return self.__str__()

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.builtin_funcs = [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl("x", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("x", IntType())], VoidType(), Block([])),
            FuncDecl("getFloat", [], FloatType(), Block([])),       
            FuncDecl("putFloat", [ParamDecl("x", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl("x", FloatType())], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putBool", [ParamDecl("x", BoolType())], VoidType(), Block([])),
            FuncDecl("putBoolLn", [ParamDecl("x", BoolType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl("x", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("x", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([])),
        ]
        self.structs = [] # list[StructType]
        self.interfaces = [] # list[InterfaceType]
        self.functions = [] # list[FuncDecl]
        self.current_func = None # FuncDecl
    
    def check(self):
        return self.visit(self.ast,[[]])

    def evaluateIntValue(self, ast, c):
        """
        :param ast: IntLiteral | Id
        :return: int
        """
        if isinstance(ast, IntLiteral):
            return int(ast.value)
        if isinstance(ast, Id):
            all_symbols = reduce(lambda acc, ele: ele + acc, c, [])
            id_symbol = self.lookup(ast.name, all_symbols, lambda x: x.name)
            if not isinstance(id_symbol.mtype, IntType):
                raise TypeMismatch(ast) #???
            # Assume that symbol is declared as Constant
            return self.evaluateIntValue(id_symbol.value, c)
        if isinstance(ast, BinaryOp):
            leftValue = self.evaluateIntValue(ast.left, c)
            rightValue = self.evaluateIntValue(ast.right, c)
            if ast.op == "+":
                return leftValue + rightValue
            if ast.op == "-":
                return leftValue - rightValue
            if ast.op == "*":
                return leftValue * rightValue
            if ast.op == "/":
                if rightValue == 0:
                    raise ZeroDivisionError
                return leftValue // rightValue
            if ast.op == "%":
                if rightValue == 0:
                    raise ZeroDivisionError
                return leftValue % rightValue
        if isinstance(ast, UnaryOp):
            bodyValue = self.evaluateIntValue(ast.body, c)
            if ast.op == "-":
                return -bodyValue
            if ast.op == "+":
                return bodyValue
        raise TypeMismatch(ast) #???
        
    def determineType(self, typ):
        """
        Determine the StructType or InterfaceType of the Id Type
        
        :param typ: Type
        :return: Type
        """
        if isinstance(typ, Id):
            user_defined_type = self.lookup(typ.name, 
                                            self.structs + self.interfaces, 
                                            lambda x: x.name)
            if user_defined_type is None:
                raise Undeclared(Type(), typ.name) #??? Not check this case
            return user_defined_type
        return typ

    def matchType(self, lhs, rhs, c, exact_same_type=True):
        """
        Compare two types
        
        :param type1: Type
        :param type2: Type
        :return: bool
        """
        lhs = self.determineType(lhs)
        rhs = self.determineType(rhs)
        #??? What to be raised when rhs is nil
        if isinstance(rhs, StructType) and rhs.name == "":
            if isinstance(lhs, (InterfaceType, StructType)):
                return True
        if not exact_same_type:
            if isinstance(lhs, InterfaceType) and isinstance(rhs, StructType):
                # the struct type implements all prototypes declared in the interface
                for prototype in lhs.methods:
                    method_decl = self.lookup(
                        prototype.name, rhs.methods, lambda x: x.fun.name)
                    if method_decl is None:
                        return False
                    if not self.matchType(prototype.retType, 
                                          method_decl.fun.retType, c):
                        return False
                    if len(prototype.params) != len(method_decl.fun.params):
                        return False
                    if not all(self.matchType(pair[0], pair[1].parType, c) 
                                for pair in zip(prototype.params, method_decl.fun.params)):
                        return False
                return True
            if isinstance(lhs, FloatType) and isinstance(rhs, IntType):
                return True
        if (isinstance(lhs, (StructType, InterfaceType)) 
            and isinstance(rhs, (StructType, InterfaceType))
        ):
            return lhs.name == rhs.name
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            # Compare the length of dimensions
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            # Compare the size of each dimension
            matchingDimens = all(
                self.evaluateIntValue(pair[0], c) == self.evaluateIntValue(pair[1], c) 
                    for pair in zip(lhs.dimens, rhs.dimens)
            )
            return (
                matchingDimens 
                and ((
                        not exact_same_type 
                        and isinstance(lhs.eleType, FloatType) 
                        and isinstance(rhs.eleType, IntType)
                    )
                    or self.matchType(lhs.eleType, rhs.eleType, c)
                )
            )
        return type(lhs) == type(rhs)

    def visitProgram(self, ast , c):
        """
        :param ast: Program
        :param c: list[list[Symbol]]"""
        # Global scope
        ## Get StructType list
        self.structs = reduce(
            lambda acc, ele: acc + [self.visit(ele, acc)], 
            filter(lambda x: isinstance(x, StructType), ast.decl), 
            []
        )
        ## Get InterfaceType list
        self.interfaces = reduce(
            lambda acc, ele: acc + [self.visit(ele, acc)],
            filter(lambda x: isinstance(x, InterfaceType), ast.decl),
            []
        )
        
        ## Get FuncDecl list (Get all functions, but not check redecalred) (Predefined Functions)
        self.functions = (
            self.builtin_funcs 
            + list(filter(lambda x: isinstance(x, FuncDecl), ast.decl))
        ) 
                        
        ## Predefined Methods
        def preVisitMethodDecl(methodDecl):
            """
            :param methodDecl: MethodDecl
            """
            # Undeclared Receiver
            receiverType = self.lookup(methodDecl.recType.name, 
                                       self.structs, 
                                       lambda x: x.name)
            if receiverType is None:
                raise Undeclared(Type(), methodDecl.recType.name) #??? Not check this case
            # Redeclared Identifier for Method/Field
            if (self.lookup(methodDecl.fun.name, 
                            receiverType.elements, lambda x: x[0]) 
                or self.lookup(methodDecl.fun.name, 
                               receiverType.methods, lambda x: x.fun.name)
            ):
                raise Redeclared(Method(), methodDecl.fun.name)
            
            # Add Names of Methods to StructType
            receiverType.methods = receiverType.methods + [methodDecl]
        list(map(
            lambda x: preVisitMethodDecl(x), 
            filter(lambda x: isinstance(x, MethodDecl), ast.decl)
        ))
        
        # Loop through FuncDecl, VarDecl, ConstDecl, MethodDecl
        c = reduce(
            lambda acc, ele: (acc[:-1] + [acc[-1] + [result]])
                if (result := self.visit(ele, acc)) is not None 
                else acc,
            self.builtin_funcs + ast.decl,
            [[]]
        )
        return c
    
    def visitParamDecl(self, ast , c):
        """
        :param ast: ParamDecl
        :param c: list[Symbol]
        :return: Symbol
        """
        # Redeclared ParamDecl
        if self.lookup(ast.parName, c[-1], lambda x: x.name) is not None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitVarDecl(self, ast, c):
        """
        :param ast: VarDecl
        :param c: list[list[Symbol]]
        :return: Symbol
        """
        # Redeclared Variable
        if self.lookup(ast.varName, c[-1], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.varName) 
        # Type Mismatch
        varInitType = self.visit(ast.varInit, c) if ast.varInit is not None else None
        if ast.varType is None:
            ast.varType = varInitType # varType and varInit cannot be both None due to syntax rule
        elif (varInitType is not None
              and not self.matchType(ast.varType, varInitType, 
                                     c, exact_same_type=False)
        ):
            raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType, ast.varInit)

    def visitConstDecl(self, ast, c):
        """
        :param ast: ConstDecl
        :param c: list[list[Symbol]]
        :return: Symbol
        """
        try:
            return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), 
                              c)
        except Redeclared as e:
            raise Redeclared(Constant(), ast.conName)
   
    def visitFuncDecl(self, ast, c):
        """
        :param ast: FuncDecl
        :param c: list[list[Symbol]]
        :return: Symbol
        """
        self.current_func = ast
        # Redeclared Function
        if self.lookup(ast.name, c[-1], lambda x: x.name) is not None:
            raise Redeclared(Function(), ast.name)
        # Redeclared ParamDecl
        c = reduce(lambda acc, ele: acc[:-1] + [acc[-1] + [self.visit(ele, acc)]], ast.params, c + [[]])
        # Redeclared in Block
        self.visit(ast.body, c)
        self.current_func = None
        return Symbol(ast.name, MType([param.parType for param in ast.params], ast.retType), None)

    def visitStructType(self, ast, c):
        """
        :param ast: StructType
        :param c: list[StructType]
        :return StructType
        """
        if c and isinstance(c[0], list):
            # Redeclared Struct name
            if self.lookup(ast.name, c[-1], lambda x: x.name) is not None:
                raise Redeclared(Type(), ast.name)
        else:
            # Redeclared Struct
            if self.lookup(ast.name, c, lambda x: x.name) is not None:
                raise Redeclared(Type(), ast.name)

        # Redeclared Field
        def visitElement(element_name, c):
            """
            :param element_name: str
            :param c: list[str]
            """
            if self.lookup(element_name, c, lambda x: x) is not None:
                raise Redeclared(Field(), element_name)
            return element_name
        reduce(lambda acc, ele: acc + [visitElement(ele, acc)], [e[0] for e in ast.elements], [])
        return ast

    def visitMethodDecl(self, ast, c):
        """
        :param ast: MethodDecl
        :param c: 
        :return MethodDecl
        """
        # Undeclard Receiver (Already checked in Program)
        # Redeclared Method/Field (Already checked in Program)
        
        self.current_func = ast.fun
        # Redeclared ParamDecl
        c = reduce(
            lambda acc, ele: acc[:-1] + [acc[-1] + [self.visit(ele, acc)]], 
            ast.fun.params, 
            c + [[Symbol(ast.receiver, ast.recType, None)]] + [[]]
        )
        # Redeclared in Block
        self.visit(ast.fun.body, c)
        self.current_func = None
        
    def visitPrototype(self, ast, c):
        """
        :param ast: Prototype
        :param c: list[Prototype]
        :return Prototype
        """
        # Redeclared Prototype
        if self.lookup(ast.name, c, lambda x: x.name) is not None:
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast, c):
        """
        :param ast: InterfaceType
        :param c: list[InterfaceType]
        :return InterfaceType
        """
        if c and isinstance(c[0], list):
            # Redeclared Interface name
            if self.lookup(ast.name, c[-1], lambda x: x.name) is not None:
                raise Redeclared(Type(), ast.name)
        else:
            # Redeclared Interface
            if self.lookup(ast.name, c, lambda x: x.name) is not None:
                raise Redeclared(Type(), ast.name)
            
        # Redeclared Prototype
        reduce(lambda acc, ele: acc + [self.visit(ele, acc)], ast.methods, [])
        return ast

    def visitForBasic(self, ast, c): 
        """
        :param ast: ForBasic
        :param c: list[list[Symbol]]
        """
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast, c): 
        """
        :param ast: ForStep
        :param c: list[list[Symbol]]
        """
        # Redeclared Variable, Type Mismatch in Init and Update
        try:
            cond = If(ast.cond, Continue(), Break())
            block = Block([ast.init, cond, ast.upda] + ast.loop.member)
            self.visit(block, c)
        except TypeMismatch as e:
            if e.err == cond:
                raise TypeMismatch(ast)
            raise e
        
    def visitForEach(self, ast, c):
        """
        :param ast: ForEach
        :param c: list[list[Symbol]]
        """
        arrType = self.visit(ast.arr, c)
        # Check type of array expr
        if not isinstance(arrType, ArrayType):
            raise TypeMismatch(ast)
        
        # Check if idx and value are declared
        # Check if idx is IntType
        if not isinstance(self.visit(ast.idx, c), IntType):
            raise TypeMismatch(ast)
        if not self.matchType(self.visit(ast.value, c), 
                              self.visit(ArrayCell(ast.arr, [IntLiteral(0)]), c), 
                              c):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitBlock(self, ast, c):
        """
        :param ast: Block
        :param c: list[list[Symbol]]
        """
        def blockReducer(acc, ele):
            if isinstance(ele, (FuncCall, MethCall)):
                result = self.visit(ele, (acc, True))
            else:
                result = self.visit(ele, acc)
            if isinstance(result, Symbol):
                return acc[:-1] + [acc[-1] + [result]]
            return acc
        reduce(blockReducer, ast.member, c + [[]])

    def visitIf(self, ast, c): 
        # Check if expr is BoolType
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        # Traverse thenStmt and elseStmt
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)
    
    def visitAssign(self, ast, c): 
        try:
            lhs_type = self.visit(ast.lhs, c)
        except Undeclared as e:
            if isinstance(ast.lhs, Id):
                # Initialized an undeclared scalar by assignment
                return self.visit(VarDecl(ast.lhs.name, None, ast.rhs), c)
            raise e
        rhs_type = self.visit(ast.rhs, c)
        if isinstance(lhs_type, VoidType):
            raise TypeMismatch(ast)
        if not self.matchType(lhs_type, rhs_type, c, exact_same_type=False):
            raise TypeMismatch(ast)
    
    def visitContinue(self, ast, c): pass
    
    def visitBreak(self, ast, c): pass
    
    def visitReturn(self, ast, c): 
        if ast.expr is None:
            if not isinstance(self.current_func.retType, VoidType):
                raise TypeMismatch(ast)
        else:
            exprType = self.visit(ast.expr, c)
            if not self.matchType(self.current_func.retType, exprType, c): 
                raise TypeMismatch(ast) 
        
    def visitBinaryOp(self, ast, c): 
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        def validType(type_list):
            """
            :param left_type: Type
            :param right_type: Type
            :param type_list: tuple[type] | type
            """
            nonlocal left_type, right_type
            return isinstance(left_type, type_list) and isinstance(right_type, type_list)
        if ast.op in ["+"]:
            if validType(StringType) or validType(FloatType) or validType(IntType): 
                return left_type
            if validType((IntType, FloatType)):
                return FloatType()
        
        elif ast.op in ["-", "*", "/"]:
            if validType(IntType) or validType(FloatType):
                return left_type
            if validType((IntType, FloatType)):
                return FloatType()
        
        elif ast.op in ["%"]:
            if validType(IntType):
                return IntType()
        
        elif ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            if validType(IntType) or validType(FloatType) or validType(StringType):
                return BoolType()
        
        elif ast.op in ["&&", "||"]:
            if validType(BoolType):
                return BoolType()
            
        raise TypeMismatch(ast)
    
    def visitUnaryOp(self, ast, c): 
        body_type = self.visit(ast.body, c)
        if ast.op in ["-", "+"] and not isinstance(body_type, (IntType, FloatType)):
            raise TypeMismatch(ast)
        if ast.op in ["!"] and not isinstance(body_type, BoolType):
            raise TypeMismatch(ast)
        return body_type
    
    def visitFuncCall(self, ast, c): 
        """
        :param ast: FuncCall
        :param c: list[list[Symbol]] | tuple(list[list[Symbol]], is_stmt: bool)
        """
        if isinstance(c, tuple):
            env = c[0]
            is_stmt = c[1]
        else:
            env = c
            is_stmt = False
            
        # Undeclared Function
        ## Function has not yet been defined
        func_decl = self.lookup(ast.funName, self.functions, lambda x: x.name) 
        if func_decl is None:
            raise Undeclared(Function(), ast.funName)
        ## Function is hidden due to the redclared identifier in local scope
        all_symbols = reduce(lambda acc, ele: ele + acc, env[1:], [])
        symbol = self.lookup(ast.funName, all_symbols, lambda x: x.name)
        if symbol is not None:
            raise Undeclared(Function(), ast.funName)
        
        # Wrong number of parameters
        if len(ast.args) != len(func_decl.params):
            raise TypeMismatch(ast)
        
        # Wrong type of parameters
        if not all(self.matchType(pair[1].parType, self.visit(pair[0], env), env) 
                    for pair in zip(ast.args, func_decl.params)):
            raise TypeMismatch(ast)
        retType = self.determineType(func_decl.retType)
        if is_stmt and not isinstance(retType, VoidType):
            raise TypeMismatch(ast)
        if not is_stmt and isinstance(retType, VoidType):
            raise TypeMismatch(ast)
        return retType
    
    def visitMethCall(self, ast, c): 
        """
        :param ast: MethCall
        :param c: list[list[Symbol]] | tuple(list[list[Symbol]], bool)
        """
        if isinstance(c, tuple):
            env = c[0]
            is_stmt = c[1]
        else:
            env = c
            is_stmt = False
        # Reciver must have StructType or InterfaceType
        receiver = self.visit(ast.receiver, env) # receiver: Type
        if not isinstance(receiver, (StructType, InterfaceType)):
            raise TypeMismatch(ast) 
        
        # Undeclared Method
        if isinstance(receiver, StructType):
            method_decl = self.lookup(ast.metName, receiver.methods, lambda x: x.fun.name)
            if method_decl is None:
                raise Undeclared(Method(), ast.metName)
            # Wrong number of parameters
            if len(ast.args) != len(method_decl.fun.params):
                raise TypeMismatch(ast)
            # Wrong type of parameters
            if not all(self.matchType(pair[1].parType, self.visit(pair[0], env), env) 
                        for pair in zip(ast.args, method_decl.fun.params)):
                raise TypeMismatch(ast)
            retType = self.determineType(method_decl.fun.retType)
        else:
            prototype = self.lookup(ast.metName, receiver.methods, lambda x: x.name)
            if prototype is None:
                raise Undeclared(Method(), ast.metName)
            # Wrong number of parameters
            if len(ast.args) != len(prototype.params):
                raise TypeMismatch(ast)
            # Wrong type of parameters
            if not all(self.matchType(pair[1], self.visit(pair[0], env), env) 
                        for pair in zip(ast.args, prototype.params)):
                raise TypeMismatch(ast)
            retType = self.determineType(prototype.retType)
        
        if is_stmt and not isinstance(retType, VoidType):
            raise TypeMismatch(ast)
        if not is_stmt and isinstance(retType, VoidType):
            raise TypeMismatch(ast)
        return retType
    
    def visitId(self, ast, c): 
        """
        :param ast: Id
        :param c: list[list[Symbol]]
        """
        # Undeclared Identifier
        all_symbols = reduce(lambda acc, ele: ele + acc, c, [])
        id_symbol = self.lookup(ast.name, all_symbols, lambda x: x.name)

        if (id_symbol is None 
            or isinstance(id_symbol, (StructType, InterfaceType)) 
            or isinstance(id_symbol.mtype, MType)
        ):
            raise Undeclared(Identifier(), ast.name)
        # StructType and InterfaceType are represented by Id
        if isinstance(id_symbol.mtype, Id):
            user_defined_type = self.lookup(id_symbol.mtype.name, self.structs + self.interfaces, lambda x: x.name)
            if user_defined_type is None:
                raise Undeclared(Type(), id_symbol.mtype.name) #??? Not check this case
            return user_defined_type
        return id_symbol.mtype
    
    def visitArrayCell(self, ast, c): 
        arrayType = self.visit(ast.arr, c)
        if not isinstance(arrayType, ArrayType):
            raise TypeMismatch(ast)
        if not all(isinstance(self.visit(x, c), IntType) for x in ast.idx):
            raise TypeMismatch(ast)
        if len(arrayType.dimens) < len(ast.idx):
            raise TypeMismatch(ast)
        if len(arrayType.dimens) > len(ast.idx):
            return ArrayType(
                arrayType.dimens[len(ast.idx):],
                arrayType.eleType
            )
        return self.determineType(arrayType.eleType)
        
    def visitFieldAccess(self, ast, c): 
        """
        :param ast: FieldAccess
        :param c: list[list[Symbol]]
        """
        receiverType = self.visit(ast.receiver, c) # receiver: Type
        if not isinstance(receiverType, StructType):
            raise TypeMismatch(ast) 
        #??? Undeclared StrucType receiver: 
        # Already checked in visitId because ast.receiver is Expr
        
        # Undeclared Field
        field = self.lookup(ast.field, receiverType.elements, lambda x: x[0])
        if field is None:
            raise Undeclared(Field(), ast.field)
        return self.determineType(field[1])

    def visitIntLiteral(self, ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c): 
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c): 
        return BoolType()
    
    def visitStringLiteral(self, ast, c): 
        return StringType()
    
    def visitArrayLiteral(self, ast, c):
        def checkElements(ele, c):
            """
            :param ele: NestedList = Union[PrimLit, List["NestedList"]]
            """
            if isinstance(ele, list):
                [checkElements(e, c) for e in ele]
            else:
                self.visit(ele, c)
        checkElements(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast, c):  
        receiverType = self.lookup(ast.name, self.structs, lambda x: x.name)
        # Undeclared StructType
        if receiverType is None:
            raise Undeclared(Type(), ast.name) #??? Not check this case
        
        # Check if all elements are declared in the struct #??? Need to check this case?
        undeclaredField = next(
            filter(
                lambda element: 
                    self.lookup(element[0], receiverType.elements, lambda x: x[0]) 
                    is None,
                ast.elements),
            None
        )
        if undeclaredField:
            raise Undeclared(Field(), undeclaredField[0])
        
        # Check all initialized fields (Undeclared or not)
        [self.visit(element[1], c) for element in ast.elements]
        return Id(ast.name)
        
    def visitNilLiteral(self, ast, c): 
        return StructType("", [], [])
        
    def visitIntType(self, ast, c): pass
    def visitFloatType(self, ast, c): pass
    def visitBoolType(self, ast, c): pass
    def visitStringType(self, ast, c): pass
    def visitVoidType(self, ast, c): pass
    def visitArrayType(self, ast, c): pass