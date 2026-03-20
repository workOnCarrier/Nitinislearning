
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
    print(f"\t received {input}")
    l, r = 0, len(input) - 1
    if input[l] == '(':
        # find the matching  ')'
        # if matching ')' is not end of exp -- assume next char as operator and evaluate the right sub string
        r = l + 1
        while r < len(input) and input[r] != ')':
            r += 1
        print(f"\t parenthesized input: {input} l: {l} \t r: {r}")
        if r == len(input) - 1:
            return calculate(input[1:len(input) - 1])
        else:
            left_input = input[1:r - 1]
            operator = input[r:r + 1]
            right_input = input[r + 2:len(input)]
            exp = Exp(operator, calculate(left_input), calculate(right_input))
            return exp.eval()
    else:
        # evaluating the core exp .. which is not expected to have either '(' or ')'
        # look for operator
        val = None
        for idx in range(len(input)):
            if input[idx] in exp_str:
                left = input[0:idx]
                right = input[idx + 1: len(input)]
                exp = Exp(input[idx], int(left), int(right))
                val = exp.eval()
                break
        if not val:
            return int(input)
        return val

def run_test(input, expected = None, expected_exception = None ):
    # try:
        res = calculate(input)
        if expected == res:
            print(f"success : {res} == {expected}")
    # except Exception as exp:
    #     print(f"internal error: {exp}")

def test_1():
    input = "5"
    expected_output = 5
    run_test(input, expected_output)
    run_test("(2+3)", 5)
    run_test("((2+3)*4)", 20)
    # run_test("(5*(2+3))", 25)
    # run_test("((5-3)*(2+3))", 25)


if __name__ == "__main__":
    test_1()