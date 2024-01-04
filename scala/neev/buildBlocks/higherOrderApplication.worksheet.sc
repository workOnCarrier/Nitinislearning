// finding fixed points


val tolerance = 0.0001

def abs(x: Double) = if x >= 0 then x else -x

def isCloseEnough(x: Double, y: Double):Boolean = {
    abs((x-y)/x) < tolerance
}

def fixedPoint ( f: Double => Double)(firstGuess: Double): Double = {
    def iterate(guess:Double): Double = 
        val next = f(guess)
        println(s"next guess: $next")
        if isCloseEnough(guess, next) then next
        else iterate (next)
    iterate(firstGuess)
}

// def sqrt(x: Double) = fixedPoint(y => ((y+x/y)/2))(0.1)

def averageDamp(f: Double => Double)(x:Double) : Double =
    (x + f(x))/2

def sqrt(x: Double) = fixedPoint(averageDamp(y=>x/y))(0.1)

var result = sqrt(2)