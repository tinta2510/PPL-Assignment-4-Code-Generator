import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """

func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
        """
        expect = """true\nfalse\ntrue\ntrue\ntrue\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_compare_string(self):
        input = """
func main() {
    var a string = "abc";
    var b string = "xyz";
    var c string = "bcd";
    var d string = "aaa";
    var e string = "abc";
    
    putBoolLn(a == e)   // true
    putBoolLn(a != b)   // true
    putBoolLn(a < c)    // true 
    putBoolLn(a <= e)   // true
    putBoolLn(a > d)    // true
    putBoolLn(a >= e)   // true
}
        """
        expect = """true\ntrue\ntrue\ntrue\ntrue\ntrue\n"""
        self.assertTrue(TestCodeGen.test(input,expect,502))
