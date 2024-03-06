



final class `02$minusSimple$minusloops$_` {
def args = `02$minusSimple$minusloops_sc`.args$
def scriptPath = """02-Simple-loops.sc"""
/*<script>*/
var x = 0

while (x < 10) {
  println(s"the square of $x is ${x * x}")
  x += 1
}

x = 0
do {
  println(s"the square of $x is ${x * x}")
  x += 1
} while (x < 10)


/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `02$minusSimple$minusloops_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `02$minusSimple$minusloops$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `02$minusSimple$minusloops_sc`.script as `02$minusSimple$minusloops`

