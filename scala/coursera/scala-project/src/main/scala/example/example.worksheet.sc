1 + 1

val x = 42

x * x
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
