


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