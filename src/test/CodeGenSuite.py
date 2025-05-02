import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_501(self):
#         input = """
# func main() {
#     putInt(10)
# }
#         """
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,501))

#     def test_502(self):
#         input = """
# func foo() int {return foo1();}
# var a = foo();
# func main() {
#     putInt(a)
#     a := foo()
#     putInt(a)
# }
# func foo1() int {return 1;}
#         """
#         expect = "11"
#         self.assertTrue(TestCodeGen.test(input,expect,502))
        
#     def test_503(self):
#         input = """
# func main() {
#     var a [2]int = [2] int {10,20};
# }
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,503))
        
#     def test_504(self):
#         input = """
# func main() {
#     var a [2][3] int = [2][3] int {{1,2,3},{4,5,6}};
# }
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,504))
        
#     def test_505(self):
#         input = """
# func main() {
#     var a [2][3] int = [2][3] int {{1,2,3},{4,5,6}};
# }
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,505))
        
#     def test_506(self):
#         input = """
# func main() {
#     var a [1] int ;
#     a[0] := 1
#     putInt(a[0]);
# }
#     """
#         self.assertTrue(TestCodeGen.test(input,"1",506))

#     def test_507(self):
#         input = """
# func main() {
#     var a [1][1][1] int  = [1][1][1] int {{{0}}};
#     a[0][0][0] := 1
#     putInt(a[0][0][0]);
# }
#     """
#         self.assertTrue(TestCodeGen.test(input,"1",507))
        
#     def test_508(self):
#         input = """
# func main() {
#     var a [1][1][1] int  = [1][1][1] int {{{0}}};
#     a[0][0] := [1]int{10};
#     putInt(a[0][0][0]);
# }
# """
#         self.assertTrue(TestCodeGen.test(input,"10",508))

#     def test_509(self):
#         input = """
# func main() {
#     if (true) {
#         putBool(true)
#     } 
# }
#     """
#         self.assertTrue(TestCodeGen.test(input,"true",509))

#     def test_510(self):
#         input = """
# func main() {
#     if (true) {
#         putBool(true)
#     } else {
#         putBool(false)     
#     }
# }
#     """
#         self.assertTrue(TestCodeGen.test(input,"true",510))

#     def test_511(self):
#         input = """
# func main() {
#     if (false) {
#         putBool(true)
#     } else {
#         putBool(false)     
#     }
# }
#     """
#         self.assertTrue(TestCodeGen.test(input,"false", 511))

    def test_512(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 512))

    def test_513(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 513))

    def test_514(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 514))