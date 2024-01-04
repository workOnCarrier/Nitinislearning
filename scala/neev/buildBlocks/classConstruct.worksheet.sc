class Rational(x: Int, y: Int) :
    require(y>0, s"denominator must be positive, was $x/$y")
    def numer = x 
    def denom = y 
    def this(x: Int) = this(x, 1)
    def add(r: Rational) = 
        Rational( numer * r.denom + denom * r.numer, denom * r.denom)
    def mul(r: Rational) = 
        Rational( numer * r.numer , denom * r.denom)
    def sub(r: Rational) = {
        Rational( (this.numer * r.denom - r.numer * this.denom ), (r.denom * this.denom))
    }
    // override def toString = s"${numer/gcd(x.abs, y)}/${denom/gcd(x.abs, y)}"
    override def toString = s"${numer/gcd(numer, denom)}/${denom/gcd(numer, denom)}"

    private def gcd(a: Int, b: Int): Int = 
        if (b == 0) then a else gcd(b.abs, (a % b).abs)
    
    def neg ( r: Rational) = Rational(-numer, denom)
    def less(that: Rational) :Boolean = numer * that.denom < that.numer * denom
    def max(that: Rational) :Rational = if (this.less(that)) then that else this
  
end Rational

extension (r:Rational)
    def min(s: Rational): Rational = if s.less(r) then s else r
    def abs: Rational = Rational(r.numer.abs, r.denom.abs)

// all operations are identifiers
extension (x: Rational)
    def + (y: Rational): Rational = x.add(y)
    def * (y: Rational): Rational = x.mul(y)
    // infix to make an alphanumeric method into a single parameter call
    infix def min2 (that: Rational): Rational = x.min(that) 

val a: Rational = Rational(1, 3)
val b: Rational = Rational(5, 7)
val c: Rational = Rational(3, 2)
val test1 = a.add(b).mul(c)
val test2 = a.sub(b)
val test3 = test2.sub(c)


// operations available due to identifier extensions
val test4 = a + b * c
// possible due to infix min2
test1 min2 test2 