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
    println("Pascal's Triangle")
    // print(s"${pascal(1, 2)} ")
    // print(s"${balance("()(()".toList)}")
    print(countChange(4, List(1,2)))
    /* for row <- 0 to 10 do
      for col <- 0 to row do
        print(s"${pascal(col, row)} ")
      println()
      */

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = 
    if ( c > r)  0 
    else if (c == 0 || r == 0) 1
    else pascal(c, r-1) + pascal(c-1, r-1)

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = 
    def checkBalance(bc: Int, chars: List[Char]): Boolean = 
      if (chars.isEmpty ) bc==0 else {
        if (bc < 0) false else {
          chars.head match{
            case '(' => checkBalance(bc+1, chars.tail)
            case ')' => checkBalance(bc-1, chars.tail)
            case _ => checkBalance(bc, chars.tail)
          }
        }
      }
    checkBalance(0, chars)

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = 
    if ( money == 0) then 1 
    else
    if (money > 0 && !coins.isEmpty) {
      countChange(money-coins.head, coins) + countChange(money, coins.tail)
    } else 0

