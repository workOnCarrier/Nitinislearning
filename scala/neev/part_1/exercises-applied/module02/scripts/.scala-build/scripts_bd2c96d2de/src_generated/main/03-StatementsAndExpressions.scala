



final class `03$minusStatementsAndExpressions$_` {
def args = `03$minusStatementsAndExpressions_sc`.args$
def scriptPath = """03-StatementsAndExpressions.sc"""
/*<script>*/
val a = 10
val b = 20

if (a > b) a else b

if (a > b) println(s"max is $a") else println(s"max is $b")

var doIt: Boolean = true
val result = while (doIt) {
  println("Hello")
  doIt = false
}

var x = 5
val y = x = 10

println(x)
println(y)

val div = 0

val n = try {
  x / div
} catch {
  case ex: ArithmeticException => 0
}

def add(a: Int, b: Int) = {
  val result = a + b
}

add(5, 6)

/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `03$minusStatementsAndExpressions_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `03$minusStatementsAndExpressions$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `03$minusStatementsAndExpressions_sc`.script as `03$minusStatementsAndExpressions`

