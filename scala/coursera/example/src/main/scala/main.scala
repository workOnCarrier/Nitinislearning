
package example

@main def run(): Unit =
    val test_list = List(1,2,3)
    println(s" max in list ${test_list} is:" + Lists.max(test_list))
    println(s" sum of elements in list ${test_list} is:" + Lists.sum(test_list))