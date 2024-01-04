package recfun

object RecFun extends RecFunInterface:

  def main(args: Array[String]): Unit =
    mainPascal(args)
    mainBalance(args)
    mainCountChange(args)
    
  def mainPascal(args: Array[String]): Unit =
    println("Pascal's Triangle")
    for row <- 0 to 10 do
      for col <- 0 to row do
        print(s"${pascal(col, row)} ")
      println()

  def mainBalance(args: Array[String]): Unit = {
    // val chars: List[Char] = "())()".toList
    val chars: List[Char] = "()()()".toList
    println(s"output of ${chars} is ${balance(chars)}")
  }

  def mainCountChange(args: Array[String]): Unit = {
    // val coins: List[Int] = List(1, 2)
    // val count = countChange(4, coins)
    val coins: List[Int] = List(500, 5, 50, 100, 20, 200, 10)
    val money: Int = 300
    val count: Int = countChange(money , coins)
    print(s"available permutations $count")
  }
  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    def listRow(row:List[Int]): List[Int] = {
      // println(s"list received: $row")
      val pairs = row.zip(row.tail)
      val internal = pairs.map( x => x._1 + x._2)
      val finalList = 1 :: internal ::: 1 :: Nil
      if ( finalList.size > r ) finalList
      else listRow(finalList)
    }
    val finalList = listRow(List(1))
    // println(s"finalList obtained: ${finalList}")
    finalList(c)
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def countParenth(chars: List[Char], count: Int): Int = {
      if (chars.isEmpty) count
      else if (count < 0) count
      else{
        chars.head match{
          case '('  => countParenth(chars.tail, count + 1)
          case ')'  => countParenth(chars.tail, count - 1)
          case _  => countParenth(chars.tail, count)
        }
      }
    }
    if (countParenth(chars, 0) == 0) true
    else false
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    var sortedCoins: List[Int] = coins.sorted
    var count: Int = 0
    def isSolution(money: Int, coins: List[Int]): Unit = {
      if (coins.isEmpty) {} // println(s"this is empty solution for money: $money")
      else{
        // println(s" obtained list: ${coins} with money: $money")
        money match{
          case money if money > coins.head => {
            isSolution(money-coins.head, coins)
            isSolution(money, coins.tail)
          }
          case _ if money == coins.head => {
            count = count + 1
            {} // println(s" \t\t found a solution where coins.head is ${coins.head}")
          }
          case money if money < coins.head => {} // println(s"failure case get money: $money with $coins")
          case money if money == 0 => {} // println("money is equal to 0")
        }
      }
    }
    isSolution(money, sortedCoins)
    count
  }
