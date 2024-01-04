1 + 1

val x = 42

x * x


def sum(xs: List[Int]): Int = {
    def sumList(acc:Int, xs: List[Int]): Int = {
      if (xs.isEmpty) acc else sumList(acc+ xs.head, xs.tail)
    }
    sumList(0, xs)
}

sum(List(1,2,3))

def max(xs: List[Int]): Int = {
    def maxList(max: Int, xs: List[Int]): Int = {
      if (xs.isEmpty) max else {
        if (max < xs.head) maxList(xs.head, xs.tail)
        else maxList(max, xs.tail)
      }
    }
    maxList(xs.head, xs.tail)
  }

max(List(1,2,3))

val list = List(1,2,3,4)
list.tail

list.sliding(2,2)
var pairs = list.zip(list.tail)

val sumPairs = pairs.map( x => x._1 + x._2 )
1 :: sumPairs ::: 1 :: Nil
sumPairs.size
sumPairs(1)


val listOfOne = List(1)
val elems = listOfOne.zip(listOfOne.tail)
val zero_elems = elems.map( x => x._1 + x._2 )
1 :: zero_elems ::: 1 :: Nil

def sqrt(x: Double) = {
  def abs(x: Double) = if (x < 0) -x else x

  def isGoodEnough(guess: Double, x: Double) =
    if (abs(guess * guess - x)/x < 0.001) true
    else false

  def improve(guess: Double, x: Double) = (guess + x / guess) / 2

  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)


  sqrtIter(1.0, x)
}

sqrt(2)
sqrt(0.1)
sqrt(0.001)
sqrt(0.1e-20)
