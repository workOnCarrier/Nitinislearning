



final class `02$minusMethodTypes$_` {
def args = `02$minusMethodTypes_sc`.args$
def scriptPath = """02-MethodTypes.sc"""
/*<script>*/
def max(x: Int, y: Int): Int =
  if (x > y) x else y

def min(x: Int, y: Int) =
  if (x < y) x else y

def sayHi(name: String): Unit =
  println(s"hello $name")

sayHi("Scala class")

def procedureSyntax(name: String) {
  println(s"hello $name")
}




/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `02$minusMethodTypes_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `02$minusMethodTypes$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `02$minusMethodTypes_sc`.script as `02$minusMethodTypes`

