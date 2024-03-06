



final class list$u002Eworksheet$_ {
def args = list$u002Eworksheet_sc.args$
def scriptPath = """list.worksheet.sc"""
/*<script>*/

val myList = List(1,4,2,3)

var newList = myList.sortBy(x=> x)

var anotherList = myList.sorted
/*</script>*/ /*<generated>*/
/*</generated>*/
}

object list$u002Eworksheet_sc {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new list$u002Eworksheet$_

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export list$u002Eworksheet_sc.script as list$u002Eworksheet

