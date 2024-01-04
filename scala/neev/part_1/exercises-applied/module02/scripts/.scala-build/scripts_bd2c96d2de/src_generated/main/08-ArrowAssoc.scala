



final class `08$minusArrowAssoc$_` {
def args = `08$minusArrowAssoc_sc`.args$
def scriptPath = """08-ArrowAssoc.sc"""
/*<script>*/
1 -> "one"

2.->("two")

ArrowAssoc(3).->("three")


// easy map iteration

val mapToRiches = Map(
  1 -> "steal underpants",
  2 -> "???",
  3 -> "profit"
)

for ((step, instruction) <- mapToRiches) {
  println(s"Step $step - $instruction")
}


/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `08$minusArrowAssoc_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `08$minusArrowAssoc$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `08$minusArrowAssoc_sc`.script as `08$minusArrowAssoc`

