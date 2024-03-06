class Rational private (val n: Int, val d: Int) {
  require(d != 0, "Zero denominator!")

  override def toString: String = s"R($n/$d)"

  def +(other: Rational): Rational =
    new Rational(
      this.n * other.d + this.d * other.n,
      this.d * other.d
    )

//  def +(i: Int): Rational = {
//    println("adding in to rational")
//    this + Rational(i)
//  } // from companion
}

object Rational {
  def apply(n: Int, d: Int): Rational =
    new Rational(n, d)

  implicit def apply(i: Int): Rational = {
    // println("converting " + i.toString + " to rational")
    new Rational(i, 1)
  }
}

val half = Rational(1, 2)

half + 5

Rational(5) + half

5 + half