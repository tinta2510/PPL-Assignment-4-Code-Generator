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

#     def test_512(self):
#         input = """
# func main() {
#     var i = 0;
#     for i < 3 {
#         putInt(i);
#         i += 1;
#     }
#     putInt(i);
# }
#         """
#         self.assertTrue(TestCodeGen.test(input, "0123", 512))

#     def test_513(self):
#         input = """
# func main() {
#     var i = 0;
#     for i < 5 {
#         if (i == 3) {
#             break;
#         }
#         putInt(i);
#         i += 1;
#     }
#     putInt(i);
# }
#         """
#         self.assertTrue(TestCodeGen.test(input, "0123", 513))

#     def test_514(self):
#         input = """
# func main() {
#     var i = 0;
#     for i < 5 {
#         i += 1;
#         if (i % 2 == 0) {
#             continue;
#         }
#         putInt(i);
#     }
#     putInt(i);
# }
#         """
#         self.assertTrue(TestCodeGen.test(input, "1355", 514))
        
#     def test_515(self):
#         input = """
# func main() {
#     var i int = 10;
#     for var i int = 0; i < 2; i += 1 {
#         putInt(i)
#         break;
#     }
#     putInt(i)
# }
#         """
#         self.assertTrue(TestCodeGen.test(input, "010", 515))
        
    # def test_516(self):
    #     input = """
    # func foo() int { return 2; }
    # func bar() int { return 3; }

    # func main() {
    #     var x = foo() + bar();
    #     putInt(x);
    # }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_517(self):
    #     input = """
    # func main() {
    #     var x = 5;
    #     if (x < 10) {
    #         if (x > 3) {
    #             putString("A");
    #         } else {
    #             putString("B");
    #         }
    #     } else {
    #         putString("C");
    #     }
    # }
    #     """
    #     expect = "A"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_518(self):
    #     input = """
    # func main() {
    #     var arr [3]int = [3]int{1,2,3};
    #     arr[1] := 10;
    #     putInt(arr[1]);
    # }
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_519(self):
    #     input = """
    # func main() {
    #     putInt(1);
    #     return;
    #     putInt(2);
    # }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_520(self):
    #     input = """
    # func main() {
    #     var a = 5;
    #     for var i = 0; i < 1; i += 1 {
    #         var a = 10;
    #         putInt(a);
    #     }
    #     putInt(a);
    # }
    #     """
    #     expect = "105"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_521(self):
    #     input = """
    # func fact(n int) int {
    #     if (n <= 1) {
    #         return 1;
    #     }
    #     return n * fact(n - 1);
    # }

    # func main() {
    #     putInt(fact(4));
    # }
    #     """
    #     expect = "24"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
        
    # def test_522(self):
    #     input = """
    # func main() {
    #     var i int;
    #     var j int;
    #     for i < 3 {
    #         j := 0;
    #         for j < 3 {
    #             if (j == 1) {
    #                 j += 1;
    #                 continue;
    #             }
    #             putInt(i*3 + j);
    #             j += 1;
    #         }
    #         i += 1;
    #     }
    # }
    #     """
    #     expect = "023568"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_523(self):
    #     input = """
    # func main() {
    #     var a [2][2]int;
    #     a[0] := [2]int{1, 2};
    #     a[1] := [2]int{3, 4};
    #     putInt(a[1][0]);
    #     putInt(a[0][1]);
    # }
    #     """
    #     expect = "32"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_524(self):
    #     input = """
    # func sideEffect() boolean {
    #     putString("called");
    #     return true;
    # }

    # func main() {
    #     var x = false || sideEffect();
    # }
    #     """
    #     expect = "called"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

#     def test_525(self):
#         input = """

# func main() {
#     var a string = "tr"
#     putStringLn("s" + a)
#     putString("s" + a + a)
# }
#         """
#         expect = "str\nstrtr"
#         self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_526(self):
        input = """
func main() {
    putBoolLn(5 > 2)
    putBoolLn(5 < 2)
    putBoolLn(5 <= 5)
    putBoolLn(5 >= 5)
    putBoolLn(5 == 5)
    putBoolLn(5 != 5)
}
        """
        expect = "true\nfalse\ntrue\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))