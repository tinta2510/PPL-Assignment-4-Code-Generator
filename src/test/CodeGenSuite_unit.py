import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """
func foo(){
    a := 5;
    putInt(a)
}

var a int = 10
        
func main(){
    foo()
    putInt(a)
}
        
    
        """
        expect = """510"""
        self.assertTrue(TestCodeGen.test(input,expect,501))
