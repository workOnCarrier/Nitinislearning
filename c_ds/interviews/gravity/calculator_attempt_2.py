
oper_amp = {'+':  lambda a,b: a + b, 
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b}

exp_str = "+-*"
exp_par_str = "()"
exp_par_start = '('
exp_par_end = ')'

class ValNode:
    def __init__(self, val):
        self.val = val
    def eval(self):
        return int(self.val)
    def __repr__(self):
        return self.val

class Parenth:
    def __init__(self):
        self.child = None
        self.closed = False
    def setChild(self, child):
        self.child = child
    def mark_close(self):
        self.closed = True
    def eval(self):
        if self.closed:
            return self.child.eval() 
        else:
            print(f"\t child: {self.child}")
            raise Exception("Evaluation parenthesis before close found")
    def __repr__(self):
        if self.closed:
            return f"({self.child})"
        else:
            return f"({self.child}"

class Exp:
    def __init__(self, oper):
        self.oper = oper
        self.left = None
        self.right = None
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def eval(self):
        if self.left is None or self.right is None:
            raise Exception (f"\t expression not formed {self.left}  -- {self.right}")
        return oper_amp[self.oper](self.left.eval(), self.right.eval())
    def __repr__(self):
        return f"{self.left} {self.oper} {self.right}"

class ExpBuilder:
    def __init__(self, input):
        self.input = input
        self.val_stack = []
        self.exp_stack_par = []
        self.exp_stack_full = []
        self.parenth_stack = []
    def build_exp(self):
        input = self.input
        cur = 0
        if input[0] != exp_par_start:
            return ValNode(input)
        while cur < len(input):
            print(f"\t {self}")
            print(f"\t ## input to process: {input[cur]}")
            if input[cur] == exp_par_start:
                self.parenth_stack.append(Parenth())
                cur += 1
            elif input[cur] == exp_par_end:
                if len(self.exp_stack_full) == 0 or len(self.parenth_stack) == 0:
                    print(f"\t exp_stack_full: {self.exp_stack_full}")
                    print(f"\t parenth_stack: {self.parenth_stack}")
                    raise Exception(f"\t unbalanced expression {input} for {input[cur]} at {cur}")
                top_parenth = self.parenth_stack.pop()
                wrapped_exp = self.exp_stack_full.pop()
                top_parenth.setChild(wrapped_exp)
                top_parenth.mark_close()
                self.exp_stack_full.append(top_parenth)
                cur += 1
            elif input[cur] in exp_str:
                exp = Exp(input[cur])
                if len(self.val_stack) > 0:
                    exp.setLeft(self.val_stack.pop())
                elif len(self.exp_stack_full) > 0:
                    exp.setLeft(self.exp_stack_full.pop())
                self.exp_stack_par.append(exp)
                cur += 1
            else:
                left_num_start = cur
                while cur < len(input) and input[cur] not in exp_str and input[cur] != exp_par_end:
                    cur += 1
                if cur == len(input):
                    raise Exception(f"unbalanced expression {input} for {left_num_start}")
                val = ValNode(input[left_num_start:cur])
                if len(self.val_stack) == 0:
                    if len(self.exp_stack_par) == 0:
                        self.val_stack.append(val)
                    else:
                        exp = self.exp_stack_par.pop()
                        exp.setRight(val)
                        self.exp_stack_full.append(exp)
                else:
                    exp = self.exp_stack_par.pop()
                    exp.setLeft(self.val_stack.pop())
                    exp.setRight(val)
                    self.exp_stack_full.append(exp)

        # check if there are remaining partial expressiolns
        if len(self.val_stack) > 0 or len(self.exp_stack_par) > 0 or len(self.parenth_stack) > 0:
            raise Exception(f" remaining unmatched parts {self}")
        print(f"\t exp_stack_full: {self.exp_stack_full}")
        return self.exp_stack_full.pop()
    def __repr__(self):
        res = f"\t val_stack: {self.val_stack}\n"
        res += f"\t exp_stack_par: {self.exp_stack_par}\n"
        res += f"\t parenth_stack: {self.parenth_stack}\n"
        res += f"\t exp_stack_full: {self.exp_stack_full}\n"
        return res



def calculate(input):
    print(f"\t received {input}")
    expbuilder = ExpBuilder(input)
    node_tree = expbuilder.build_exp()
    result = node_tree.eval()
    return result



def run_test(input, expected = None, expected_exception = None ):
    # try:
        res = calculate(input)
        if expected == res:
            print(f"success : {res} == {expected} for input: {input}")
    # except Exception as exp:
    #     print(f"internal error: {exp}")

def test_1():
    input = "5"
    expected_output = 5
    # run_test(input, expected_output)
    # run_test("(2+3)", 5)
    # run_test("((2+3)*4)", 20)
    # run_test("(5*(2+3))", 25)
    # run_test("((5-3)*(2+3))", 25)


if __name__ == "__main__":
    test_1()