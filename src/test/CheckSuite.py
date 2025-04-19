import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class io {} """
        input = """class io {}"""
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class abc { }
        class def {}
        class abc{}"""
        expect = "Redeclared Class: abc"
        self.assertTrue(TestChecker.test(input,expect,301))
    
    def test_simple_program_using_ast(self):
        input = Program([ClassDecl(Id("io"),[])])
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,302))

    def test_complex_program_using_ast(self):
        input = Program([ClassDecl(Id("abc"),[]),
            ClassDecl(Id("def"),[]),
            ClassDecl(Id("abc"),[])])
        expect = "Redeclared Class: abc"
        self.assertTrue(TestChecker.test(input,expect,303))
   