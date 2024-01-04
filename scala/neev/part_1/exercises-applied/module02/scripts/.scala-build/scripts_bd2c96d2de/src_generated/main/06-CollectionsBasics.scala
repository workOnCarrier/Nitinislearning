



final class `06$minusCollectionsBasics$_` {
def args = `06$minusCollectionsBasics_sc`.args$
def scriptPath = """06-CollectionsBasics.sc"""
/*<script>*/
val array1: Array[Int] = Array(1,2,3)
val list1: List[String] = List("scooby", "dooby", "doo")

val array2 = Array(1,2,3)
val list2 = List("scooby", "dooby", "doo")

def squareRootsOf(xs: List[Int]): List[Double] = {
  for (x <- xs) yield math.sqrt(x)
}

squareRootsOf(List(1,2,3,4,5,6))

// type parameters are not optional, this will not compile:
// def badSquareRootsOf(xs: List): List = {
//   for (x <- xs) yield math.sqrt(x)
// }

// List initializers

val lista = List(1,2,3)

val listb = 4 :: 5 :: 6 :: Nil

val listc = lista ::: listb

// common beginner mistake:

// val listd = lista :: listb

val v = Vector(1,2,3,4)

def squareRootOfAll(xs: Seq[Int]): Seq[Double] =
  xs.map(x => math.sqrt(x))

squareRootOfAll(v)
squareRootOfAll(listc)
squareRootOfAll(array2)


val set1 = Set(1,2,3,1,2,4,5)

// squareRootOfAll(set1) // does not compile

/*</script>*/ /*<generated>*/
/*</generated>*/
}

object `06$minusCollectionsBasics_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `06$minusCollectionsBasics$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `06$minusCollectionsBasics_sc`.script as `06$minusCollectionsBasics`

