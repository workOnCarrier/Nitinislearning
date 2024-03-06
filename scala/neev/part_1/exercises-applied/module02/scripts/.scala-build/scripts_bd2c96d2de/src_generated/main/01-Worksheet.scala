



final class `01$minusWorksheet$_` {
def args = `01$minusWorksheet_sc`.args$
def scriptPath = """01-Worksheet.sc"""
/*<script>*/
val x = 10

var y = x * 2

y = 11

for (i <- 1 to 10) yield i * 2

def max(x: Int, y: Int): Int =
  if (x > y) x else y

max(x, y)
max(4, 8)


/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `01$minusWorksheet_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `01$minusWorksheet$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `01$minusWorksheet_sc`.script as `01$minusWorksheet`

