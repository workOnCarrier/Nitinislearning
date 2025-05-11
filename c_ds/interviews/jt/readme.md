Consider a workflow management system that allows clients to compose "tasks". Each task is a function that accepts the following arguments in the following order:
1. exactly one argument (called "input") in position 0,
2. zero or more additional positional arguments,
3. zero or more keyword arguments
and returns a single value of the same type as "input". In this way any number of tasks can be chained together. For example:
task3(task2(task1 (input)), arg1, kwarg2=1)
Clients use the following syntax to specify tasks and whether to chain them together in series or in parallel.
(Whitespace in the specification is ignored.)
1. Comma-separated tasks are composed in series.
- client specification: task1,task2,task3
- resulting code
  
   task3(task2(task1 (input))
2. Semicolon-separated tasks within curly braces are composed in parallel, which yields multiple code paths.
- client specification: task1,{task2;task3)
- resulting code
  
   : task2(task1 (input))
  
   task3(task1 (input))
Note that the empty string is a valid task in a parallel context:
- client specification: task1,task2,{task3;}
- resulting code
: task3(task2(task1 (input)))
task2(task1(input))
It's guaranteed that composition via comma will not occur inside parallel clause. I.e. {task1;task2,task3) (note the comma instead of semicolon) is not a valid input.
3. A task's positional and keyword arguments (if any) are comma-separated and appended in parentheses following that task's name.
- client specification: task1 ('b',kw=1), task2(1,2,var1='a')
- resulting code
: task2(task1 (input,b',kw=1),1,2,var1=a)
4. Multiple parallel branches compound when listed serially.
- client specification: {func1;func2), (func3;func4)
- resulting code
: func3(func1 (input))
func4(func1 (input))
func3(func2(input))
func4(func2(input))
You have been given a parser for this specification, but the parser has bugs and your job is to fix it. Two "TODO" comments already mark areas where there are known issues. There is at least one additional unmarked bug.
Note that the parser intentionally strips all whitespace from the input and includes a new line before each expansion in the output.
You may want to copy the starter code into a separate buffer for future reference. You are also not required to use any of the starter code.