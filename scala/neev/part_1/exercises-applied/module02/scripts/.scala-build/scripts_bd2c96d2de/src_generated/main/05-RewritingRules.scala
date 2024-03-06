



final class `05$minusRewritingRules$_` {
def args = `05$minusRewritingRules_sc`.args$
def scriptPath = """05-RewritingRules.sc"""
/*<script>*/
val x = 1 + 2

val y = 1.+(2)

val s = "hello"

s.charAt(1)
s charAt 1

// println "hello" // will not compile

System.out println "hello"

// --- apply and update

val arr = Array("scooby", "dooby", "doo")

arr.apply(1)

arr(0)


arr.update(0, "scrappy")

arr(1) = "dappy"

println(arr.deep)

val arr2 = Array.apply(1,2,3)

val z = 10
// z(2) // does not compile

val xs = List(1,2,3)
xs(1)  // works
// xs(1) = 10 // does not compile

var xs2 = Array(1,2,3)
xs2(1)  // works
xs2(1) = 10 // does not compile


/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `05$minusRewritingRules_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `05$minusRewritingRules$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `05$minusRewritingRules_sc`.script as `05$minusRewritingRules`

