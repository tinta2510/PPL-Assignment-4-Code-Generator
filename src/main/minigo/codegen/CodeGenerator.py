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
        
    def initValue(self, typ):
        if isinstance(typ, IntType):
            return IntLiteral(0)
        elif isinstance(typ, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(typ, BoolType):
            return BooleanLiteral(True)
        elif isinstance(typ, StringType):
            return StringLiteral('""')
        elif isinstance(typ, ArrayType):
            def init_list(shape, value=0):
                if len(shape) == 0:
                    return value
                return [init_list(shape[1:], value) for _ in range(int(shape[0]))]
            return ArrayLiteral(
                typ.dimens,
                typ.eleType,
                init_list(list(map(lambda x: x.value, typ.dimens)), 
                          self.initValue(typ.eleType)) #???
            )
    
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
            "<init>", MType([], VoidType()), False, frame))  
        frame.enterScope(True) 
         
        # Create "this" variable in the <init> method
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), "this", ClassType(self.className), 
            frame.getStartLabel(), frame.getEndLabel(), frame))  
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
        
    def emitObjectClassInit(self,ast, o):
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD(
            "<clinit>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        #TODO: Initialize global/static vars  #???
        o['frame'] = frame
        self.visit(Block([Assign(Id(item.varName), item.varInit) 
                          for item in ast.decl if isinstance(item, VarDecl) and item.varInit]),
                   o)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        

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
        env = {}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # Body of the program
        env = reduce(
            lambda acc, ele: self.visit(ele, acc), 
            list(filter(lambda x: isinstance(x, VarDecl), ast.decl))
                + list(filter(lambda x: isinstance(x, FuncDecl), ast.decl)), 
            env)
        self.emitObjectInit()
        self.emitObjectClassInit(ast, env)
        
        self.emit.printout(self.emit.emitEPILOG())
        return env

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
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Body of the method
        env['env'] = [[]] + env['env'] # Scope for parameters
        if isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(), "args", ArrayType([None],StringType()), 
                    frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc), ast.params, env)
        self.visit(ast.body, env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(ast.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitVarDecl(self, ast, o):
        if not ast.varInit:
            ast.varInit = self.initValue(ast.varType)
        
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
            varInitCode, varInitType = self.visit(ast.varInit, o)
            
            self.emit.printout(self.emit.emitVAR(
                index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if isinstance(ast.varType, FloatType) and isinstance(varInitType, IntType):
                ast.varInit = FloatLiteral(float(ast.varInit.value))
            if ast.varInit:
                self.emit.printout(varInitCode)
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
        return o
    
    def visitConstDecl(self, ast: ConstDecl, o):
        # TODO: Declare var as final
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, self.functions), None)
        env = o.copy()
        env['isLeft'] = False
        argsCode = [self.visit(x, env)[0] for x in ast.args]
        invokeCode = self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, env['frame'])
        if env.get('isStmt', None) and env['isStmt'] == True:
            [self.emit.printout(x) for x in argsCode + [invokeCode]]
            return o
        else: # FuncCall is expr
            return "".join(argsCode + [invokeCode]), sym.mtype.rettype
    
    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        def blockReducer(env, ele):
            if isinstance(ele, FuncCall):
                env['isStmt'] = True
            else:
                env['isStmt'] = False
            return self.visit(ele, env)
        env = reduce(blockReducer, ast.member, env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, 
                          [i for lst in o['env'] for i in lst]), 
                   None)
        if isinstance(sym.value, Index):
            func = self.emit.emitWRITEVAR if o['isLeft'] else self.emit.emitREADVAR
            return (func(ast.name, sym.mtype, sym.value.value, o['frame']), 
                    sym.mtype)
        else:    
            func = self.emit.emitPUTSTATIC if o['isLeft'] else self.emit.emitGETSTATIC     
            return (func(f"{self.className}/{sym.name}", sym.mtype, o['frame']), 
                    sym.mtype)
    
    def visitAssign(self, ast, o):
        # Initialize the variable if it hasn't been declared yet
        if (isinstance(ast.lhs, Id) 
            and not ast.lhs.name in [i.name for lst in o["env"] for i in lst]
        ):
            return self.visit(VarDecl(ast.lhs.name, None, ast.rhs))
        if isinstance(ast.lhs, ArrayCell):
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, o)
        else:
            o['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, o)            
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)        
        
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
    
    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast, o):
        if isinstance(ast.value, bool):
            ast.value = "true" if ast.value else "false"
        return (self.emit.emitPUSHICONST(ast.value, o['frame']), 
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
                if not (o.get('isLeft') and o['isLeft'] == True):
                    code += self.emit.emitALOAD(retType, o['frame'])
                return code, retType
            else:
                code += self.emit.emitALOAD(arrType, o['frame'])
                arrType = ArrayType(arrType.dimens[1:], arrType.eleType)
    
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
        o['frame'].enterLoop()
        loopLabel = o['frame'].getNewLabel()
        continueLabel = o['frame'].getContinueLabel()
        exitLabel = o['frame'].getBreakLabel()
        
        # Init code
        self.visit(ast.init, o)
        # LOOP (CONTINUE) LABEL
        self.emit.printout(self.emit.emitLABEL(loopLabel, o['frame']))
        # Condition code
        condCode, condType = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        # If condition is false, exit the loop
        self.emit.printout(self.emit.emitIFFALSE(exitLabel, o['frame']))
        # Body code
        self.visit(ast.loop, o)
        # Continue label
        self.emit.printout(self.emit.emitLABEL(continueLabel, o['frame']))
        # Update counter code
        self.visit(ast.update, o)
        # GOTO loopLabel
        self.emit.printout(self.emit.emitGOTO(str(loopLabel), o['frame']))
        # Exit label
        self.emit.printout(self.emit.emitLABEL(exitLabel, o['frame']))
        
        o['frame'].exitLoop()
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
    