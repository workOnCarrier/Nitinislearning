
oper_amp = {'+':  lambda a,b: a + b, 
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b}

exp_str = "+,*"

class Exp:
    def __init__(self, oper, par1, par2):
        self.oper = oper
        self.left = par1
        self.right = par2
    def eval(self):
        return oper_amp[self.oper](self.left, self.right)

def calculate(input):
    l, r = 0, len(input) - 1
    if input[l] == '(':
        # find the maptching  ')'
        # if matching ')' is not end of exp -- assume next char as operator and evaluate the right sub string
        r = l + 1
        while r < len(input) and r != ')':
            r += 1
        if r = len(input) -1:
            return calculate(input[1:len(input) -1 ])
        else:
            left_input = input[1:len(input) -1]
            operator = input[r + 1]
            right_input = input[r + 1:len(input)]
        

    else:
        # evaluating the core exp .. which is not expected to have either '(' or ')'

    if '(' in subexp:
        # find closing ')' ...
        # we have operator just after that
        # on right of the operator can be start of another '(' 
    else:
        # look for operator
        for idx in range(len(subexp)):
            if subexp[idx] in exp_str:
                left = subexp[0:idx]
                right = subexp[idx + 1: len(subexp)]
                exp = Exp(subexp[idx], left, right)
                val = exp.eval
                break

def run_test(input, expected = None, expected_exception = None ):
    try:
        res = calculate(input)
        if expected == res:
            print(f"success : {res} == {expected}")
    except Exception exp:
        if expected_exception
        print(f"internal error: {exp}")

def test_1():
    input = "5"
    expected_output = 5
    run_test(input, expected_output)
    run_test("(2+3)", 5)
    run_test("((2+3)*4)", 20)
    run_test("(5*(2+3))", 25)
    run_test("((5-3)*(2+3))", 25)


if __name__ == "__main__":
    test_1()