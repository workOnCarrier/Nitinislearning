
def sumInts(a: Int, b: Int): Int = 
    if (a > b) then 0 else a + sumInts(a+1, b)


def cube (x: Int): Int = x*x*x

def sumCubes(a: Int, b: Int): Int = 
    if a > b then 0 else cube(a) + sumCubes(a+1, b)

def fact(a:Int): Int = 
    if a == 1 then 1 else a * fact(a-1)

def sumFactorial(a: Int, b: Int): Int = 
    if a > b then 0 else fact(a) + sumFactorial(a+1, b)

sumFactorial(1, 4)
sumCubes(1,3)

def summation(f: Int => Int, a: Int, b: Int) : Int = 
    if a > b then 0 else f(a) + summation(f, a+1, b)

val cubeSum = summation(x => x * x * x, 1, 3)
val factSum = summation(fact, 1, 4)

def tailRecSum(f: Int => Int, a: Int, b: Int): Int = 
    def loop(a: Int, acc: Int): Int =
        if a > b then acc
        else loop(a+1, acc+f(a))
    loop(a, 0)

val newCubeSum = tailRecSum(x => x * x * x, 1, 3)

def funcReturnFunc(f: Int => Int) : (Int, Int) => Int =
    def genSum(a: Int, b: Int) : Int =
        if a > b then 0
        else f(a) + genSum(a+1, b)
    genSum

val funCubeSum = funcReturnFunc(fact)(1,4)

def curriedFun(f: Int => Int)(a: Int,b: Int): Int =
    // def genSum(a: Int, b: Int) : Int =
        if a > b then 0
        else f(a) + curriedFun(f)(a+1, b) // else f(a) + genSum(a+1, b)
    // genSum

val curriedCubSum = curriedFun(z => z * z * z)(1,3)


def products(f: Int=> Int)(a: Int, b: Int): Int =
    if a > b then 1 else f(a) * products(f)(a+1, b)

val newFactVal = products(x => x)(1, 4)

def newFact(n: Int) = products(x => x)(1, n)

val factWithProd = newFact(4)

def genAccum ( f: Int => Int, oper: (Int, Int)=> Int, default: Int)(a: Int, b: Int): Int =
    def recur(a: Int): Int = 
        if a > b then default else oper(f(a), genAccum(f, oper, default)(a+1, b))
    recur(a)

def crazyFact(n: Int) = genAccum(z => z, (x, y) => x * y, 1)(1, n)
// def sumFactCrazy(n: Int) = genAccum(z => crazyFact(z), (x, y) => x + y, 0)(1, n)
def sumFactCrazy(n: Int) = genAccum(z => genAccum(z => z, (x, y)=> x*y, 1)(1,z), (x, y) => x + y, 0)(1, n)
def sumN(n: Int) = genAccum(z => z, (x , y) => x + y, 0) (1, n)
def sumFunc(f: Int => Int) = genAccum(f, (x , y) => x + y, 0)
def newSumN(n: Int) = sumFunc(x => x)(1, n)

val sumWithCrazy = sumN(4)
val sumWithNewSumN = newSumN(4)
val factWithCrazy = crazyFact(4)
val sumFactWithCrazy = sumFactCrazy(5)
val splitUpFactSum = sumFunc(crazyFact)(1,5)
