



final class `01$minusIntro$minusto$minusScala$_` {
def args = `01$minusIntro$minusto$minusScala_sc`.args$
def scriptPath = """01-Intro-to-Scala.sc"""
/*<script>*/
1 + 2

val x = 1 + 2

x * 2

// x = x * 2   // will not compile, try it

var y = 2

y = y * 2

// y = "four"  // also will not compile - types must be the same

def add(x: Int, y: Int) = x + y

add(2, 3)

def addAgain(x: Int, y: Int): Int = {
  x + y
}

addAgain(2, 3)

val a = 10
val b = 12

if (a > b) {
  println(a)
}
else {
  println(b)
}

val m = if (a > b) a else b

def maxSquaredDoubled(a: Int, b: Int): Int =
  if (a > b) {
    val squared = a * a
    squared * 2
  }
  else {
    val squared = b * b
    squared * 2
  }

maxSquaredDoubled(5, 3)

val divided = try {
  a / (b - 12)
}
catch {
  case ae: ArithmeticException => 0
}



/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `01$minusIntro$minusto$minusScala_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `01$minusIntro$minusto$minusScala$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `01$minusIntro$minusto$minusScala_sc`.script as `01$minusIntro$minusto$minusScala`

