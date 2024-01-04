



final class matchcase$_ {
def args = matchcase_sc.args$
def scriptPath = """matchcase.sc"""
/*<script>*/



// no default case
def checkMatchSign(value: Int): Unit = {
    value match{
        case x if x > 0 =>  println("value greater than 0")
        case x if x < 0 =>  {
            println(s"value less than 0 $x")
            checkMatchSign(x+1)
        }
        case 0 => println("value equal than 0")
    }
}

def testCheckMatch(): Unit = {
    checkMatchSign(1)
    checkMatchSign(0)
    checkMatchSign(-3)
}

val nothing =    testCheckMatch()
println(nothing)
/*</script>*/ /*<generated>*/
/*</generated>*/
}

object matchcase_sc {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new matchcase$_

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export matchcase_sc.script as matchcase

