import unittest
from TestUtils import TestCodeGen
from AST import *
import inspect

class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """
    func main() {
        putInt(42)
    }
        """
        expect = "42"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_502(self):
        input = """
    func main() {
        var a = 3;
        var b = 4;
        putInt(a + b);
    }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_503(self):
        input = """
    func main() {
        var a = 10;
        if (a > 5) {
            putString("big");
        }
    }
        """
        expect = "big"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_504(self):
        input = """
    func main() {
        var arr [3]int = [3]int{5,6,7};
        putInt(arr[1]);
    }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_505(self):
        input = """
    func main() {
        var a = true;
        putBool(a);
    }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_506(self):
        input = """
    func main() {
        var a = false;
        if (!a) {
            putString("ok");
        }
    }
        """
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_507(self):
        input = """
    func add(a int, b int) int {
        return a + b;
    }
    func main() {
        putInt(add(2, 3));
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_508(self):
        input = """
    func main() {
        var s = "Hi";
        putString(s + "!");
    }
        """
        expect = "Hi!"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_509(self):
        input = """
    func main() {
        var i = 0;
        for i < 2 {
            putInt(i);
            i += 1;
        }
    }
        """
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_510(self):
        input = """
    func main() {
        var a = 5;
        var b = 2;
        putInt(a * b);
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_511(self):
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
    }
        """
        expect = "012"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_512(self):
        input = """
    func main() {
        var i = 0;
        for i < 4 {
            i += 1;
            if (i % 2 == 0) {
                continue;
            }
            putInt(i);
        }
    }
        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_513(self):
        input = """
    func main() {
        var arr [2]int = [2]int{1, 2};
        arr[0] := 5;
        putInt(arr[0]);
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_514(self):
        input = """
    func add(a int, b int) int {
        return a + b;
    }
    func main() {
        var res = add(10, add(2, 3));
        putInt(res);
    }
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_515(self):
        input = """
    func main() {
        var a = 10;
        if (a > 5) {
            if (a < 20) {
                putString("ok");
            }
        }
    }
        """
        expect = "ok"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_516(self):
        input = """
    func main() {
        var x = 1;
        var y = 2;
        var z = 3;
        if (x < y && y < z) {
            putString("yes");
        }
    }
        """
        expect = "yes"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_517(self):
        input = """
    func square(n int) int {
        return n * n;
    }
    func main() {
        var result = square(6);
        putInt(result);
    }
        """
        expect = "36"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_518(self):
        input = """
    func main() {
        var s = "a";
        for var i = 0; i < 3; i += 1 {
            s := s + "b";
        }
        putString(s);
    }
        """
        expect = "abbb"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_519(self):
        input = """
    func main() {
        var a = 3;
        var b = 4;
        var c = 5;
        if (a * a + b * b == c * c) {
            putString("pythagoras");
        }
    }
        """
        expect = "pythagoras"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_520(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_521(self):
        input = """
    func inc(x int) int {
        return x + 1;
    }
    func main() {
        var a = 5;
        a := inc(a);
        putInt(a);
    }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_522(self):
        input = """
    func main() {
        var a = 3;
        if (a % 2 == 1) {
            putString("odd");
        } else {
            putString("even");
        }
    }
        """
        expect = "odd"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_523(self):
        input = """
    func main() {
        var s = "code";
        s := s + "gen";
        putString(s);
    }
        """
        expect = "codegen"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_524(self):
        input = """
    func mul(a int, b int) int {
        return a * b;
    }
    func main() {
        var x = mul(2, 3);
        var y = mul(x, 2);
        putInt(y);
    }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_525(self):
        input = """
    func main() {
        var arr [2]int = [2]int{0, 0};
        arr[0] := 7;
        arr[1] := arr[0] + 1;
        putInt(arr[1]);
    }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_526(self):
        input = """
    func main() {
        var i = 0;
        for i < 3 {
            if (i == 1) {
                i += 1;
                continue;
            }
            putInt(i);
            i += 1;
        }
    }
        """
        expect = "02"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_527(self):
        input = """
    func main() {
        var sum = 0;
        for var i = 1; i <= 3; i += 1 {
            sum := sum + i;
        }
        putInt(sum);
    }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 527))


    def test_528(self):
        input = """
    func main() {
        var a = 1;
        var b = 2;
        putInt(a + b);
    }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_529(self):
        input = """
    func main() {
        var a = true;
        putBool(!a);
    }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_530(self):
        input = """
    func add(a int, b int) int {
        return a + b;
    }
    func main() {
        putInt(add(3, 4));
    }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_531(self):
        input = """
    func main() {
        var a string = "Hi, ";
        var b string = "there!";
        putString(a + b);
    }
        """
        expect = "Hi, there!"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_532(self):
        input = """
    func main() {
        var a = 5;
        if (a > 3) {
            putString("greater");
        }
    }
        """
        expect = "greater"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_533(self):
        input = """
    func main() {
        var i = 0;
        for i < 2 {
            putInt(i);
            i += 1;
        }
    }
        """
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_534(self):
        input = """
    func main() {
        var a [3]int = [3]int{1,2,3};
        putInt(a[2]);
    }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_535(self):
        input = """
    func main() {
        var a = 5;
        var b = 10;
        var c = a * b;
        putInt(c);
    }
        """
        expect = "50"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_536(self):
        input = """
    func main() {
        var flag = false;
        if (!flag) {
            putString("off");
        }
    }
        """
        expect = "off"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_537(self):
        input = """
    func main() {
        var x = 2;
        var y = 3;
        var z = x * x + y * y;
        putInt(z);
    }
        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input, expect, 537))
        
    def test_538(self):
        input = """
    type Point struct {x int; y int;}

    func main() {
        var p Point = Point{x: 1, y: 2};
        putInt(p.x + p.y);
    }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_539(self):
        input = """
    type Point struct {x int; y int;}

    func main() {
        var p Point;
        p.x := 5;
        p.y := 7;
        putInt(p.x * p.y);
    }
        """
        expect = "35"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_540(self):
        input = """
    type Speaker interface {speak();}

    type Dog struct {}

    func (d Dog) speak() {
        putString("woof");
    }

    func main() {
        var s Speaker = Dog{};
        s.speak();
    }
        """
        expect = "woof"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_541(self):
        input = """
    type Data struct {val int;}

    func main() {
        var d Data = Data{val: 9};
        d.val := d.val + 1;
        putInt(d.val);
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_542(self):
        input = """
    type Greeter interface {greet();}
    type Person struct {name string;}

    func (p Person) greet() {
        putString("Hello, " + p.name);
    }

    func main() {
        var g Greeter = Person{name: "Alice"};
        g.greet();
    }
        """
        expect = "Hello, Alice"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_543(self):
        input = """
    type Counter struct {value int;}

    func (c Counter) next() int {
        return c.value + 1;
    }

    func main() {
        var c Counter = Counter{value: 99};
        putInt(c.next());
    }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_544(self):
        input = """
    type Point struct {x int; y int;}

    func (p Point) sum() int {
        return p.x + p.y;
    }

    func main() {
        var pt = Point{x: 3, y: 4};
        putInt(pt.sum());
    }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_545(self):
        input = """
    type Shape interface {area() int;}
    type Square struct {side int;}

    func (s Square) area() int {
        return s.side * s.side;
    }

    func main() {
        var s Shape = Square{side: 4};
        putInt(s.area());
    }
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = """
    type Box struct {w int; h int;}

    func (b Box) area() int {
        return b.w * b.h;
    }

    func main() {
        var b Box = Box{w: 2, h: 5};
        putInt(b.area());
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_547(self):
        input = """
    type A struct {val int;}
    type B struct {a A;}

    func main() {
        var b B = B{a: A{val: 7}};
        putInt(b.a.val);
    }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_548(self):
        input = """
    type Speaker interface {speak();}
    type Cat struct {name string;}

    func (c Cat) speak() {
        putString("Meow, " + c.name);
    }

    func main() {
        var s Speaker = Cat{name: "Milo"};
        s.speak();
    }
        """
        expect = "Meow, Milo"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_549(self):
        input = """
    type Math struct {a int; b int;}

    func (m Math) add() int {
        return m.a + m.b;
    }

    func main() {
        var m = Math{a: 6, b: 7};
        putInt(m.add());
    }
        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_550(self):
        input = """
    type Pair struct {first int; second int;}

    func swap(p Pair) Pair {
        return Pair{first: p.second, second: p.first};
    }

    func main() {
        var p = Pair{first: 1, second: 2};
        var q = swap(p);
        putInt(q.first); putInt(q.second);
    }
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_551(self):
        input = """
    type Rect struct {w int; h int;}

    func (r Rect) area() int {
        return r.w * r.h;
    }

    func main() {
        var r Rect = Rect{w: 3, h: 7};
        var a = r.area();
        putInt(a);
    }
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_552(self):
        input = """
    type Num struct {val int;}

    func double(n Num) int {
        return n.val * 2;
    }

    func main() {
        var x = Num{val: 9};
        var y = double(x);
        putInt(y);
    }
        """
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_553(self):
        input = """
    func main() {
        var s = "a";
        for var i = 0; i < 2; i += 1 {
            s := s + "b";
        }
        putString(s);
    }
        """
        expect = "abb"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_554(self):
        input = """
    func fib(n int) int {
        if (n <= 1) {
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }

    func main() {
        putInt(fib(5));
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_555(self):
        input = """
    type Counter struct {val int;}

    func (c Counter) inc() Counter {
        return Counter{val: c.val + 1};
    }

    func main() {
        var c = Counter{val: 1};
        c := c.inc();
        c := c.inc();
        putInt(c.val);
    }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_556(self):
        input = """
    type Container struct {data [2]int;}

    func main() {
        var c = Container{data: [2]int{4, 5}};
        c.data[1] := 10;
        putInt(c.data[0] + c.data[1]);
    }
        """
        expect = "14"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_557(self):
        input = """
    func sum(n int) int {
        var total = 0;
        for var i = 1; i <= n; i += 1 {
            total := total + i;
        }
        return total;
    }

    func main() {
        putInt(sum(4));
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_558(self):
        input = """
    type Printer interface {print();}

    type Data struct {val int;}

    func (d Data) print() {
        putInt(d.val);
    }

    func main() {
        var p Printer = Data{val: 123};
        p.print();
    }
        """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_559(self):
        input = """
    func isEven(n int) boolean {
        return n % 2 == 0;
    }

    func main() {
        if (isEven(6)) {
            putString("even");
        } else {
            putString("odd");
        }
    }
        """
        expect = "even"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_560(self):
        input = """
    type Vec2 struct {x int; y int;}

    func (v Vec2) magnitudeSquared() int {
        return v.x * v.x + v.y * v.y;
    }

    func main() {
        var v = Vec2{x: 3, y: 4};
        putInt(v.magnitudeSquared());
    }
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_561(self):
        input = """
    type Item struct {id int;}

    func main() {
        var items [2]Item = [2]Item{Item{id: 1}, Item{id: 2}};
        putInt(items[1].id);
    }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_562(self):
        input = """
    type Group struct {nums [3]int;}

    func main() {
        var g = Group{nums: [3]int{1,2,3}};
        g.nums[0] := 5;
        putInt(g.nums[0]);
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_563(self):
        input = """
    type Person struct {name string; age int;}

    func (p Person) isAdult() boolean {
        return p.age >= 18;
    }

    func main() {
        var p = Person{name: "Tom", age: 20};
        if (p.isAdult()) {
            putString("yes");
        } else {
            putString("no");
        }
    }
        """
        expect = "yes"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_564(self):
        input = """
    func factorial(n int) int {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    func main() {
        putInt(factorial(4));
    }
        """
        expect = "24"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_565(self):
        input = """
    type Speaker interface {speak();}
    type Robot struct {id int;}

    func (r Robot) speak() {
        putString("ID:");
        putInt(r.id);
    }

    func main() {
        var s Speaker = Robot{id: 7};
        s.speak();
    }
        """
        expect = "ID:7"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_566(self):
        input = """
    func max(a int, b int) int {
        if (a > b) {
            return a;
        }
        return b;
    }

    func main() {
        putInt(max(9, 4));
    }
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_567(self):
        input = """
    type Calc struct {a int; b int;}

    func (c Calc) eval() int {
        return (c.a + c.b) * 2;
    }

    func main() {
        var c = Calc{a: 2, b: 3};
        putInt(c.eval());
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_568(self):
        input = """
    type Logger interface {log();}
    type Debugger struct {msg string;}

    func (d Debugger) log() {
        putString(d.msg);
    }

    func main() {
        var l Logger = Debugger{msg: "debug"};
        l.log();
    }
        """
        expect = "debug"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_569(self):
        input = """
    func sumArray(arr [3]int) int {
        return arr[0] + arr[1] + arr[2];
    }

    func main() {
        var a = [3]int{2, 4, 6};
        putInt(sumArray(a));
    }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_570(self):
        input = """
    type Wrapper struct {val int;}

    func update(w Wrapper) Wrapper {
        return Wrapper{val: w.val + 10};
    }

    func main() {
        var w = Wrapper{val: 5};
        w := update(w);
        putInt(w.val);
    }
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_571(self):
        input = """
    type Pair struct {a int; b int;}

    func (p Pair) swap() Pair {
        return Pair{a: p.b, b: p.a};
    }

    func main() {
        var p = Pair{b: 9, a: 2};
        var q = p.swap();
        putInt(q.a); putInt(q.b);
    }
        """
        expect = "92"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_572(self):
        input = """
    type Acc struct {total int;}

    func (a Acc) add(x int) Acc {
        return Acc{total: a.total + x};
    }

    func main() {
        var a = Acc{total: 1};
        a := a.add(2);
        a := a.add(3);
        putInt(a.total);
    }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_573(self):
        input = """
    func power(base int, exp int) int {
        if (exp == 0) {
            return 1;
        }
        return base * power(base, exp - 1);
    }

    func main() {
        putInt(power(2, 4));
    }
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_574(self):
        input = """
    type Printer interface {print();}
    type Msg struct {text string;}

    func (m Msg) print() {
        putString(m.text);
    }

    func main() {
        var m = Msg{text: "done"};
        var p Printer = m;
        p.print();
    }
        """
        expect = "done"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_575(self):
        input = """
    type Container struct {data [2]int;}

    func main() {
        var c = Container{data: [2]int{3, 4}};
        c.data[0] := c.data[1] + 1;
        putInt(c.data[0]);
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_576(self):
        input = """
    func sumEven(n int) int {
        var s = 0;
        for var i = 0; i <= n; i += 1 {
            if (i % 2 == 0) {
                s := s + i;
            }
        }
        return s;
    }

    func main() {
        putInt(sumEven(6));
    }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_577(self):
        input = """
    type Counter struct {val int;}

    func (c Counter) inc() Counter {
        return Counter{val: c.val + 1};
    }

    func main() {
        var a = [2]Counter{Counter{val: 0}, Counter{val: 1}};
        a[1] := a[1].inc();
        putInt(a[1].val);
    }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_578(self):
        input = """
    type Adder struct {a int; b int;}

    func (x Adder) sum() int {
        return x.a + x.b;
    }

    func main() {
        var x = [1]Adder{Adder{a: 10, b: 15}};
        putInt(x[0].sum());
    }
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_579(self):
        input = """
    func main() {
        var i = 0;
        var acc = 1;
        for i < 3 {
            acc := acc * 2;
            i := i + 1;
        }
        putInt(acc);
    }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_580(self):
        input = """
    type User struct {name string;}

    func greet(u User) string {
        return "Hello, " + u.name;
    }

    func main() {
        var u = User{name: "Dana"};
        var msg = greet(u);
        putString(msg);
    }
        """
        expect = "Hello, Dana"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_581(self):
        input = """
    type Rect struct {w int; h int;}

    func (r Rect) perimeter() int {
        return 2 * (r.w + r.h);
    }

    func main() {
        var r = Rect{w: 4, h: 5};
        putInt(r.perimeter());
    }
        """
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_582(self):
        input = """
    type Mult struct {val int;}

    func (m Mult) apply(x int) int {
        return m.val * x;
    }

    func main() {
        var m = Mult{val: 3};
        putInt(m.apply(6));
    }
        """
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_583(self):
        input = """
    func maxOfThree(a int, b int, c int) int {
        var max int;
        if (a > b && a > c) {
            max := a;
        } else {
            if (b > c) {
                max := b;
            } else {
                max := c;
            }
        }
        return max;
    }

    func main() {
        putInt(maxOfThree(3, 9, 6));
    }
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_584(self):
        input = """
    type IntArray struct {arr [3]int;}

    func (ia IntArray) sum() int {
        return ia.arr[0] + ia.arr[1] + ia.arr[2];
    }

    func main() {
        var x = IntArray{arr: [3]int{2, 4, 6}};
        putInt(x.sum());
    }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_585(self):
        input = """
    type Entity interface {info();}

    type Hero struct {name string; power int;}

    func (h Hero) info() {
        putString(h.name);
        putInt(h.power);
    }

    func main() {
        var e Entity = Hero{name: "A", power: 10};
        e.info();
    }
        """
        expect = "A10"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_586(self):
        input = """
    func multiplyThenAdd(a int, b int, c int) int {
        return a * b + c;
    }

    func main() {
        var res = multiplyThenAdd(2, 3, 4);
        putInt(res);
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_587(self):
        input = """
    type Wrapper struct {n int;}

    func (w Wrapper) double() Wrapper {
        return Wrapper{n: w.n * 2};
    }

    func main() {
        var w = Wrapper{n: 5};
        w := w.double();
        putInt(w.n);
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_588(self):
        input = """
    func countOdds(n int) int {
        var count = 0;
        for var i = 0; i <= n; i += 1 {
            if (i % 2 == 1) {
                count := count + 1;
            }
        }
        return count;
    }

    func main() {
        putInt(countOdds(7));
    }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_589(self):
        input = """
    type Coord struct {x int; y int;}

    func (c Coord) reflectY() Coord {
        return Coord{x: -c.x, y: c.y};
    }

    func main() {
        var p = Coord{x: 5, y: 2};
        var q = p.reflectY();
        putInt(q.x); putInt(q.y);
    }
        """
        expect = "-52"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_590(self):
        input = """
    type Shape interface {area() int;}

    type Square struct {side int;}
    type Rect struct {w int; h int;}

    func (s Square) area() int { return s.side * s.side; }
    func (r Rect) area() int { return r.w * r.h; }

    func main() {
        var s Shape = Square{side: 4};
        var r Shape = Rect{w: 2, h: 3};
        putInt(s.area());
        putInt(r.area());
    }
        """
        expect = "166"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_591(self):
        input = """
    type Student struct {name string; grade int;}

    func (s Student) passed() boolean {
        return s.grade >= 50;
    }

    func main() {
        var s = Student{name: "Linh", grade: 70};
        if (s.passed()) {
            putString("yes");
        } else {
            putString("no");
        }
    }
        """
        expect = "yes"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_592(self):
        input = """
    type Number struct {value int;}

    func (n Number) triple() int {
        return n.value * 3;
    }

    func main() {
        var n = Number{value: 5};
        putInt(n.triple());
    }
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_593(self):
        input = """
    func gcd(a int, b int) int {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    func main() {
        putInt(gcd(28, 12));
    }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_594(self):
        input = """
    type Pos struct {x int; y int;}

    type Box struct {
        topLeft Pos;
        width int;
        height int;
    }

    func (b Box) area() int {
        return b.width * b.height;
    }

    func main() {
        var b = Box{topLeft: Pos{x: 0, y: 0}, width: 5, height: 6};
        putInt(b.area());
    }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_595(self):
        input = """
    type A interface {f() int;}
    type B struct {val int;}

    func (b B) f() int {
        return b.val + 1;
    }

    func main() {
        var x A = B{val: 9};
        putInt(x.f());
    }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_596(self):
        input = """
    type Wrapper struct {arr [3]int;}

    func (w Wrapper) sum() int {
        return w.arr[0] + w.arr[1] + w.arr[2];
    }

    func main() {
        var w = Wrapper{arr: [3]int{1, 1, 1}};
        putInt(w.sum());
    }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_597(self):
        input = """
    func countDiv(n int, d int) int {
        var cnt = 0;
        for var i = 1; i <= n; i += 1 {
            if (i % d == 0) {
                cnt := cnt + 1;
            }
        }
        return cnt;
    }

    func main() {
        putInt(countDiv(10, 2));
    }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_598(self):
        input = """
    type Transformer struct {base int;}

    func (t Transformer) apply(x int) int {
        return (x + t.base) * 2;
    }

    func main() {
        var t = Transformer{base: 3};
        putInt(t.apply(4));
    }
        """
        expect = "14"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_599(self):
        input = """
    type Talker interface {talk();}

    type Human struct {msg string;}
    func (h Human) talk() { putString(h.msg); }

    type Bot struct {code int;}
    func (b Bot) talk() { putInt(b.code); }

    func main() {
        var a Talker = Human{msg: "hi"};
        var b Talker = Bot{code: 404};
        a.talk();
        b.talk();
    }
        """
        expect = "hi404"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_600(self):
        input = """
    type Stats struct {x int; y int;}

    func (s Stats) avg() int {
        return (s.x + s.y) / 2;
    }

    func main() {
        var s = Stats{x: 6, y: 8};
        putInt(s.avg());
    }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 600))
