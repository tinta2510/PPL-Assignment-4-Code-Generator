import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """

type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
    var a PPL3 = PPL3 {number: 10}
    putIntLn(a.number)
    a.study()
}
    
        """
        expect = """10\n10"""
        self.assertTrue(TestCodeGen.test(input,expect,501))
