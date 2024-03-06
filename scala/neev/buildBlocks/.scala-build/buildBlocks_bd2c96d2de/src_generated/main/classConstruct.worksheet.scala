



final class classConstruct$u002Eworksheet$_ {
def args = classConstruct$u002Eworksheet_sc.args$
def scriptPath = """classConstruct.worksheet.sc"""
/*<script>*/
class Rational(x: Int, y: Int) {
    def numer = x
    def denom = y
    def add(r: Rational) = 
        Rational( numer * r.denom + denom * r.numer, denom * r.denom)
    def mul(r: Rational) = 
        Rational( numer * r.numer , denom * r.denom)
    override def toString = s"$numer/$denom"
  
}




val a: Rational = Rational(1, 3)
val b: Rational = Rational(5, 7)
val c: Rational = Rational(3, 2)
val newVal = a.add(b).mul(c)
println(newVal)

/*</script>*/ /*<generated>*/
/*</generated>*/
}

object classConstruct$u002Eworksheet_sc {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new classConstruct$u002Eworksheet$_

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export classConstruct$u002Eworksheet_sc.script as classConstruct$u002Eworksheet

