# value categories

<https://en.cppreference.com/w/cpp/language/value_category.html>
* lvalue -- a glvalue that is not xvalue
    * glvalue -- (generalized lvalue) an expression whose evaluation determines the identity of an object or function
    * xvalue -- (expiring glvalue) expiring value is a glvalue that denotes and object whose resources can be reused
* rvalue -- is a prvalue or an xvalue
    * prvalue -- pure rvalue : an expression whose evaluation
        - computes teh value of an operand of a built-in operator : has no result object
        - initializes an object : has a result object
