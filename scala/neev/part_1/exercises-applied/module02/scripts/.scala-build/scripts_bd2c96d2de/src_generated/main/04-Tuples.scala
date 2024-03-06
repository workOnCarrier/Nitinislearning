



final class `04$minusTuples$_` {
def args = `04$minusTuples_sc`.args$
def scriptPath = """04-Tuples.sc"""
/*<script>*/
def sumAndDifference(a: Int, b: Int): (Int, Int) = {
  val sum = a + b
  val difference = a - b
  (sum, difference)
}

val res = sumAndDifference(10, 5)

res._1
res._2

val (sm, df) = sumAndDifference(10, 5)

val (a,b,c,d,e) = (0, 'u', 8, 1, "too")



/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `04$minusTuples_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `04$minusTuples$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `04$minusTuples_sc`.script as `04$minusTuples`

