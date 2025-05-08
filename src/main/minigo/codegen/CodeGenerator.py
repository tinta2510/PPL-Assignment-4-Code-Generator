'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from functools import reduce
from abc import ABC, abstractmethod
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
    
    def init(self):
        mem = [
            Symbol("getInt",MType([],IntType()),CName("io",True)),
            Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
            Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
            Symbol("getFloat",MType([],FloatType()),CName("io",True)),
            Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
            Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
            Symbol("getBool",MType([],BoolType()),CName("io",True)),
            Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
            Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
            Symbol("getString",MType([],StringType()),CName("io",True)),
            Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
            Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
            Symbol("putLn",MType([],VoidType()),CName("io",True)),
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD(
            "<init>", MType([], VoidType()), False, False, frame))  
        frame.enterScope(True) 
         
        # Create "this" variable in the <init> method
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), "this", Id(self.className), 
            frame.getStartLabel(), frame.getEndLabel(), frame))  
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        self.emit.printout(self.emit.emitREADVAR("this", Id(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
        
    def emitObjectClassInit(self,ast, o):
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD(
            "<clinit>", MType([], VoidType()), False, False, frame))
        frame.enterScope(True)
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        o['frame'] = frame
        self.visit(Block(
            [Assign(Id(item.varName), item.varInit) 
                for item in ast.decl if isinstance(item, VarDecl) and item.varInit]
            + [Assign(Id(item.conName), item.iniExpr)
                for item in ast.decl if isinstance(item, ConstDecl)]), o)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
    # --- Visit Declarations - START ---
    def visitProgram(self, ast, c):
        """
        Args:
        - c(list[list[Symbol]]): Symbol table
        """
        self.functions = (
            c + [Symbol(decl.name, 
                        MType(list(map(lambda param_decl: param_decl.parType, decl.params)), 
                                decl.retType), 
                        CName(self.className)
                    ) for decl in filter(lambda x: isinstance(x, FuncDecl), ast.decl)])
        self.structs = list(filter(lambda x: isinstance(x, StructType), ast.decl))
        self.interfaces = list(filter(lambda x: isinstance(x, InterfaceType), ast.decl))
        def addMethodDecl(methodDecl):
            """
            Add method declaration to the struct type
            """
            receiverType = self.lookup(methodDecl.recType.name, 
                                       self.structs, 
                                       lambda x: x.name)
            # Add Names of Methods to StructType
            receiverType.methods = receiverType.methods + [methodDecl]
        [addMethodDecl(methodDecl) 
         for methodDecl in filter(lambda x: isinstance(x, MethodDecl), ast.decl)]
        
        env = {}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # Body of the program
        env = reduce(
            lambda acc, ele: self.visit(ele, acc), 
            list(filter(lambda x: isinstance(x, (VarDecl, ConstDecl)), ast.decl))
                + list(filter(lambda x: isinstance(x, FuncDecl), ast.decl)), 
            env)
        self.emitObjectInit()
        self.emitObjectClassInit(ast, env)
        
        self.emit.printout(self.emit.emitEPILOG())
        
        # Create Jasmin file of structs and interfaces
        self.curr_struct = None
        def visitType(typ):
            self.curr_struct = typ
            self.emit = Emitter(self.path + "/" + typ.name + ".j") 
            self.visit(typ, {'env': env['env']})
        [visitType(typ) for typ in self.interfaces + self.structs]
        return env
    
    def _initValue(self, typ):
        if isinstance(typ, IntType):
            return IntLiteral(0)
        elif isinstance(typ, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(typ, BoolType):
            return BooleanLiteral(True)
        elif isinstance(typ, StringType):
            return StringLiteral('""')
        elif isinstance(typ, ArrayType): 
            return ArrayLiteral(
                typ.dimens,
                typ.eleType,
                []
            )
        elif isinstance(typ, (ClassType, Id)):
            return StructLiteral(typ.name, [])
        return None
    
    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        # Add function to symbol table 
        o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(
            ast.name, mtype, True, False, frame))
        frame.enterScope(True)
        
        # Body of the method
        env['env'] = [[]] + env['env'] # Scope for parameters
        ## .var directive for parameters
        if isMain:
            self.emit.printout(self.emit.emitVAR(
                frame.getNewIndex(), "args", ArrayType([None],StringType()), 
                frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc), ast.params, env)
        ## Code for the body of the method
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.visit(ast.body, env)        
        if isinstance(ast.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitVarDecl(self, ast, o):
        if not ast.varInit:
            ast.varInit = self._initValue(ast.varType)
        
        # get rhs type
        env = o.copy()
        # Create a virtual frame
        if not ast.varType:
            env['frame'] = Frame('virtual_frame', VoidType()) 
            varInitCode, varInitType = self.visit(ast.varInit, env)
            ast.varType = varInitType

        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(
                ast.varName, ast.varType, True, False, None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
            varInitCode, varInitType = self.visit(ast.varInit, o) if ast.varInit else (None, None)
            
            self.emit.printout(self.emit.emitVAR(
                index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if isinstance(ast.varType, FloatType) and isinstance(varInitType, IntType):
                ast.varInit = FloatLiteral(float(ast.varInit.value))
            if ast.varInit:
                self.emit.printout(varInitCode)
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
        return o
    
    def visitConstDecl(self, ast, o):
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def visitParamDecl(self, ast: ParamDecl, o):        
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(
            index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))  
        return o
    
    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        def visitStmt(stmt):
            if isinstance(stmt, (FuncCall, MethCall)):
                env['isStmt'] = True
            else:
                env['isStmt'] = False
            self.visit(stmt, env)
        [visitStmt(stmt) for stmt in ast.member]
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitMethodDecl(self, ast, o):
        # Create frame for the method
        frame = Frame(ast.fun.name, ast.fun.retType)
        env = o.copy()
        env['frame'] = frame
        # Jasmin code for the method
        mtype = MType(
            [x.parType for x in ast.fun.params], ast.fun.retType)
        self.emit.printout(self.emit.emitMETHOD(
            ast.fun.name, mtype, False, False, frame))
        frame.enterScope(True)
        
        # Body of the method
        env['env'] = [[]] + env['env']
        ## .var
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), "this", Id(self.curr_struct.name),
            frame.getStartLabel(), frame.getEndLabel(), frame))
        env = reduce(lambda acc,e: self.visit(e,acc), ast.fun.params, env)
        ## Code for the body of the method
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        ### Case when the method is a constructor
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR(
                "this", Id(self.curr_struct.name), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.visit(ast.fun.body, env)
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitPrototype(self, ast, o):
        frame = Frame(ast.name, ast.retType)
        self.emit.printout(self.emit.emitMETHOD(
            ast.name, MType(ast.params, ast.retType), False, True, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame, True))
        return o
    # --- Visit Declarations - END ---
    
    # --- Visit Expressions - START ---
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, self.functions), None)
        # Visit the arguments
        env = o.copy()
        env['isLeft'] = False
        env['isStmt'] = False   
        argsCode = [self.visit(x, env)[0] for x in ast.args]
        # Invoke the function
        invokeCode = self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
        code = argsCode + [invokeCode]
        if o.get('isStmt', False):
            [self.emit.printout(x) for x in code]
            return o
        else: # FuncCall is expr
            return "".join(code), sym.mtype.rettype
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, 
                          [i for lst in o['env'] for i in lst]), 
                   None)
        if sym is None: # "this" variable
            # "this" is only used as RHS
            return (self.emit.emitREADVAR("this", Id(""), 0, o['frame']), 
                    Id(self.curr_struct.name))
        if isinstance(sym.value, Index):
            func = self.emit.emitWRITEVAR if o.get('isLeft', False) else self.emit.emitREADVAR
            return (func(ast.name, sym.mtype, sym.value.value, o['frame']), 
                    sym.mtype)
        else:    
            func = self.emit.emitPUTSTATIC if o.get('isLeft', False) else self.emit.emitGETSTATIC     
            return (func(f"{self.className}/{sym.name}", sym.mtype, o['frame']), 
                    sym.mtype)
            
    def visitUnaryOp(self, ast, o):
        if ast.op in ["+", "-"]:
            bodyCode, typ = self.visit(ast.body, o)
            negCode = self.emit.emitNEGOP(typ, o['frame']) if ast.op == "-" else ""
            return bodyCode + negCode, typ
        elif ast.op == "!":
            bodyCode, typ = self.visit(ast.body, o)
            notCode = self.emit.emitNOT(typ, o['frame'])
            return bodyCode + notCode, typ
          
    def visitBinaryOp(self, ast, o):
        leftCode, leftType = self.visit(ast.left, o)
        rightCode, rightType = self.visit(ast.right, o)

        retType = None
        if ast.op in ["+", "-", "*", "/"]:
            if ast.op in ["+", "-"]:
                op = self.emit.emitADDOP
            elif ast.op in ["*", "/"]:
                op = self.emit.emitMULOP
            
            if type(leftType) != type(rightType):
                if isinstance(leftType, IntType):
                    leftCode += self.emit.emitI2F(o['frame'])
                if isinstance(rightType, IntType):
                    rightCode += self.emit.emitI2F(o['frame'])
                retType = FloatType()
            else:
                retType = leftType
            opCode = op(ast.op, retType, o['frame'])
        elif ast.op == "%":
            retType = IntType()
            opCode = self.emit.emitMOD(o['frame'])
        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            retType = BoolType()
            opCode = self.emit.emitREOP(ast.op, retType, o['frame'])
        elif ast.op in ["&&", "||"]:
            retType = BoolType()
            if ast.op == "&&":
                opCode = self.emit.emitANDOP(o['frame'])
            else:
                opCode = self.emit.emitOROP(o['frame'])
        return leftCode + rightCode + opCode, retType
    
    def visitArrayCell(self, ast, o):
        code = ""
        # Code to get the array address
        env = o.copy()
        env['isLeft'] = False
        arrAddrCode, arrType = self.visit(ast.arr, env)
        code += arrAddrCode
        
        for i, idx in enumerate(ast.idx):
            idxCode, idxType = self.visit(idx, env)
            code += idxCode
            if i == len(ast.idx) - 1:
                retType = None
                if len(arrType.dimens) == 1:
                    retType = arrType.eleType
                else:
                    retType = ArrayType(arrType.dimens[1:], arrType.eleType)
                if not (o.get('isLeft', False)):
                    code += self.emit.emitALOAD(retType, o['frame'])
                return code, retType
            else:
                code += self.emit.emitALOAD(arrType, o['frame'])
                arrType = ArrayType(arrType.dimens[1:], arrType.eleType)
                
    def visitFieldAccess(self, ast, o):
        # receiverClass is Id object
        env = o.copy()
        env['isLeft'] = False
        receiverCode, receiverClass = self.visit(ast.receiver, env) 
        # receiverType is StructType object
        receiverType = self.lookup(receiverClass.name, self.structs, lambda x: x.name)
        # elements:List[Tuple[str,Type]] in StructType
        fieldType = self.lookup(ast.field, receiverType.elements, 
                                lambda x: x[0])[1]
        # Swap for LHS case
        swapCode = self.emit.emitSWAP() if o.get('isLeft', False) else ""
        # Code to put/get field
        op = (self.emit.emitPUTFIELD if o.get('isLeft', False) 
              else self.emit.emitGETFIELD)
        fieldCode = op(f"{receiverClass.name}/{ast.field}", fieldType, o['frame'])
        return receiverCode + swapCode +  fieldCode, fieldType
    
    def visitMethCall(self, ast, o):
        # receiverClass is Id object
        receiverCode, receiverClass = self.visit(ast.receiver, o) 
        # receiverType is StructType/InterfaceType object
        receiverType = self.lookup(receiverClass.name, self.structs + self.interfaces, 
                                   lambda x: x.name)
        # Create virtual env for visiting args of MethCall
        env = o.copy()
        env['isLeft'] = False
        env['isStmt'] = False   
        # Visit the arguments
        argsCode = [self.visit(x, env)[0] for x in ast.args]
        if isinstance(receiverType, StructType):
            methDecl = self.lookup(ast.metName, receiverType.methods, lambda x: x.fun.name)
            mtype = MType([x.parType for x in methDecl.fun.params], methDecl.fun.retType)
            invokeCode = self.emit.emitINVOKEVIRTUAL(
                f"{receiverClass.name}/{ast.metName}", mtype, o['frame'])
        else: # isinstance(receiverType, InterfaceType)
            prototype = self.lookup(ast.metName, receiverType.methods, lambda x: x.name)
            mtype = MType(prototype.params, prototype.retType)
            invokeCode = self.emit.emitINVOKEINTERFACE(
                f"{receiverClass.name}/{ast.metName}", mtype, o['frame'])
        code = [receiverCode] + argsCode + [invokeCode]
        if o.get('isStmt', False):
            [self.emit.printout(x) for x in code]
            return o
        else: # MethCall is expr
            return "".join(code), mtype.rettype
    # --- Visit Expressions - END ---
    
    # --- Visit Literals - START ---
    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast, o):
        return (self.emit.emitPUSHCONST(ast.value, BoolType(), o['frame']), 
                BoolType())
        
    def visitStringLiteral(self, ast, o):
        return (self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), 
                StringType())
        
    def visitArrayLiteral(self, ast, o):
        retType = ArrayType(ast.dimens, ast.eleType)
        code = ""
        code += "".join([self.visit(dim, o)[0] for dim in ast.dimens])
        if len(ast.dimens) == 1: # 1D array
            code += self.emit.emitNEWARRAY(ast.eleType, o['frame'])
        else: # MultiD array
            code += self.emit.emitMULTIANEWARRAY(retType, len(ast.dimens), o['frame'])
        def reduceArray(arr, index, emitArrCode):
            """
            Args:
            - arr(list): array
            - index(int): index of the array
            - emitArrCode(list): code to load the array
            """
            code = ""
            if isinstance(arr[index], list):
                subArrayCode = [
                    # Push the accessde index
                    f"self.emit.emitPUSHCONST({index}, IntType(), o['frame'])",
                    # Load the sub-array
                    f"self.emit.emitALOAD(ArrayType(None, None), o['frame'])"]
                code += "".join([reduceArray(arr[index], i, emitArrCode + subArrayCode) for i in range(len(arr[index]))])
            else:
                # Code to access the array address
                code += "".join([eval(c) for c in emitArrCode])
                # Push index to the stack
                code += self.emit.emitPUSHCONST(index, IntType(), o['frame'])
                # Get the assgined value
                assignedValue = self.visit(arr[index], o)
                code += assignedValue[0]
                # Store the value to the array
                code += self.emit.emitASTORE(assignedValue[1], o['frame'])
            return code
        code += "".join([reduceArray(ast.value, i, ["self.emit.emitDUP(o['frame'])"]) 
                         for i in range(len(ast.value))])
        return code, retType
    
    def visitStructLiteral(self, ast, o):
        code = self.emit.emitNEW(Id(ast.name), o['frame'])
        code += self.emit.emitDUP(o['frame'])

        env = o.copy()
        env['isLeft'] = False
        env['isStmt'] = False
        
        # Find the struct declaration
        structType = self.lookup(ast.name, self.structs, lambda x: x.name)
        # Initialize non-initialized elements
        def initElement(ele):
            if ele[0] in [i[0] for i in ast.elements]:
                return self.lookup(ele[0], ast.elements, lambda x: x[0])
            return ele[0], self._initValue(ele[1])
        initedElements = [initElement(ele) for ele in structType.elements]
        # Visit the expression of elements of the struct literal
        visitedElements = [self.visit(ele[1], env) for ele in initedElements]
        code += "".join([ele[0] for ele in visitedElements])
        code += self.emit.emitINVOKESPECIAL(
            o['frame'], f"{ast.name}/<init>", 
            MType([ele[1] for ele in visitedElements], VoidType()))
        return code, Id(ast.name)
    
    def visitNilLiteral(self, ast, o):
        return self.emit.emitACONST_NULL(o['frame']), Id("")
    # -- Visit Literals - END ---
                
    # --- visit Statements - START ---
    def visitAssign(self, ast, o):
        # Initialize the variable if it hasn't been declared yet
        if (isinstance(ast.lhs, Id) 
            and not ast.lhs.name in [i.name for lst in o["env"] for i in lst]
        ):
            return self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)
        env = o.copy()
        if isinstance(ast.lhs, ArrayCell):
            env['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, env)
            env['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, env)
        else: # Include FieldAccess case
            env['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, env)            
            env['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, env)        
        
        # Co-erce
        if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
            rhsCode += self.emit.emitI2F(o['frame'])
        # Print code
        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(lhsCode + rhsCode 
                               + self.emit.emitASTORE(lhsType, o['frame']))
        else:
            self.emit.printout(rhsCode + lhsCode)
        return o
    
    def visitReturn(self, ast, o):
        typ = VoidType()
        if ast.expr:
            code, typ = self.visit(ast.expr, o)
            self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(typ, o['frame']))
        return o
    
    def visitIf(self, ast, o):
        elseLabel = o['frame'].getNewLabel()
        endLabel = o['frame'].getNewLabel()
        # Expr code
        exprCode, exprType = self.visit(ast.expr, o)
        self.emit.printout(exprCode)
        # If code
        self.emit.printout(self.emit.emitIFFALSE(
            elseLabel if ast.elseStmt else endLabel, o['frame']))
        # Then code
        self.visit(ast.thenStmt, o)
        if ast.elseStmt:
            # GOTO endLabel
            self.emit.printout(self.emit.emitGOTO(str(endLabel), o['frame']))
            # Else Label
            self.emit.printout(self.emit.emitLABEL(elseLabel, o['frame']))
            # Else code
            self.visit(ast.elseStmt, o) if ast.elseStmt else None
        # End Label
        self.emit.printout(self.emit.emitLABEL(endLabel, o['frame']))
        return o

    def visitForBasic(self, ast, o):
        o['frame'].enterLoop()
        loopLabel = o['frame'].getContinueLabel()
        exitLabel = o['frame'].getBreakLabel()
        
        # LOOP (CONTINUE) LABEL
        self.emit.printout(self.emit.emitLABEL(loopLabel, o['frame']))
        # Condition code
        condCode, condType = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        # If condition is false, exit the loop
        self.emit.printout(self.emit.emitIFFALSE(exitLabel, o['frame']))
        # Body code
        self.visit(ast.loop, o)
        # GOTO loopLabel
        self.emit.printout(self.emit.emitGOTO(str(loopLabel), o['frame']))
        # Exit label
        self.emit.printout(self.emit.emitLABEL(exitLabel, o['frame']))
        
        o['frame'].exitLoop()
        return o
    
    def visitForStep(self, ast, o):
        self.visit(
            Block([ast.init, 
                   ForBasic(ast.cond, Block(ast.loop.member+[ast.upda]))]), 
            o)
        return o
    
    def visitForEach(self, ast, o):
        # Not need to implement
        return o
    
    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(
            str(o['frame'].getContinueLabel()), o['frame']))
        return o
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(
            str(o['frame'].getBreakLabel()), o['frame']))
        return o
    # --- visit Statements - END ---
    
    # --- visit Types - START ---
    def _matchType(self, lhs, rhs, exact_same_type=True):
        """
        Compare two types
        
        :param type1: Type
        :param type2: Type
        :return: bool
        """
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
                    if not self._matchType(prototype.retType, 
                                          method_decl.fun.retType):
                        return False
                    if len(prototype.params) != len(method_decl.fun.params):
                        return False
                    if not all(self._matchType(pair[0], pair[1].parType) 
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
                #!!! Hard code to compare the size of each dimension
                # Assume the size of each dimension is an IntLit
                (not isinstance(pair[0], IntLiteral) 
                 or not isinstance(pair[1], IntLiteral)
                 or int(pair[0].value) == (pair[1].value)) 
                    for pair in zip(lhs.dimens, rhs.dimens)
            )
            return (
                matchingDimens 
                and ((
                        not exact_same_type 
                        and isinstance(lhs.eleType, FloatType) 
                        and isinstance(rhs.eleType, IntType)
                    )
                    or self._matchType(lhs.eleType, rhs.eleType)
                )
            )
        return type(lhs) == type(rhs)
    
    def visitStructType(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))
        # .implements <interface_name>     
        for interface in self.interfaces:
            if self._matchType(interface, ast, False):
                ast.implements.append(interface)
                self.emit.printout(self.emit.emitIMPLEMENTS(interface.name))
                
        # .field 
        [self.emit.printout(self.emit.emitATTRIBUTE(
            ele[0], ele[1], False, False, None)) for ele in ast.elements]
        
        # .method
        ## Method constructor with parameter
        if len(ast.elements) > 0:
            self.visit(
                MethodDecl(None, None, 
                        FuncDecl("<init>", 
                                    [ParamDecl(ele[0], ele[1]) for ele in ast.elements],
                                    VoidType(), 
                                    Block([Assign(FieldAccess(Id(""), ele[0]), 
                                                Id(ele[0])) 
                                        for ele in ast.elements]))), 
                o)
        ## Method constructor without parameter
        self.visit(
            MethodDecl(None, None, 
                       FuncDecl("<init>", [], VoidType(), Block([]))), 
            o)
        
        ## Method declarations
        [self.visit(meth_decl, o) for meth_decl in ast.methods]
        
        self.emit.printout(self.emit.emitEPILOG())
    
    def visitInterfaceType(self, ast, o):
        self.emit.printout(self.emit.emitINTERFACE(ast.name, "java.lang.Object"))
        [self.visit(prototype, o) for prototype in ast.methods]
        self.emit.printout(self.emit.emitEPILOG())
    # -- visit Types - END ---