



final class higherOrderApplication$u002Eworksheet$_ {
def args = higherOrderApplication$u002Eworksheet_sc.args$
def scriptPath = """higherOrderApplication.worksheet.sc"""
/*<script>*/
// finding fixed points


val tolerance = 0.0001

def abs(x: Double) = if x >= 0 then x else -x

def isCloseEnough(x: Double, y: Double):Boolean = {
    abs((x-y)/x) < tolerance
}

def fixedPoint ( f: Double => Double)(firstGuess: Double): Double = {
    def iterate(guess:Double): Double = 
        val next = f(guess)
        println(s"next guess: $next")
        if isCloseEnough(guess, next) then next
        else iterate (next)
    iterate(firstGuess)
}

// def sqrt(x: Double) = fixedPoint(y => ((y+x/y)/2))(0.1)

def averageDamp(f: Double => Double)(x:Double) : Double =
    (x + f(x))/2

def sqrt(x: Double) = fixedPoint(averageDamp(y=>x/y))(0.1)

var result = sqrt(2)
/*</script>*/ /*<generated>*/
/*</generated>*/
}

object higherOrderApplication$u002Eworksheet_sc {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new higherOrderApplication$u002Eworksheet$_

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export higherOrderApplication$u002Eworksheet_sc.script as higherOrderApplication$u002Eworksheet

