# The stack organization is very effective in evaluating arithmetic expressions. Expressions are usually represented in what is known as Infix notation, in which each operator is written between two operands(i.e., A + B). With this notation, we must distinguish between(A + B)*C and A + (B * C) by using either parentheses or some operator-precedence convention. Thus, the order of operators and operands in an arithmetic expression does not uniquely determine the order in which the operations are to be performed.


def compare(op1, op2):
    """
    Comparison of two operators priority, higher priority than multiplication and division subtraction
         op1 higher priority than the returns True op2, otherwise it returns False
    """
    return op1 in ["*", "/"] and op2 in ["+", "-"]


def getvalue(num1, num2, operator):
    """
         According to the results and return to operator operation symbol
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:  # /
        return num1 / num2


def process(data, opt):
    """
         opt out of an operator stack, the stack two data values, calculated once, and the result stack data
    """
    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(getvalue(num1, num2, operator))


def calculate(s):
    """
         Value calculating a string expression, the string does not contain spaces
    """
    data = []  # Data Stack
    opt = []  # operator stack
    i = 0  # traversing the index expression
    while i < len(s):
        if s[i] .isdigit():  # number, data stack
            start = i  # numeric character start position
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
                data.append (int (s [start: i + 1])) # i as the last digit character position
        elif s [i] == ")": # right parenthesis, opt out of the stack while the stack data and computed results data stack, the stack until a left parenthesis opt
            while opt[-1] != "(":
                process(data, opt)
                opt.pop () # popped "("
        elif not opt ​​or opt [-1] == "(": # operator stack is empty, or the top of the stack to the left bracket operator, the operator directly push opt
            opt.append(s[i])
        elif s [i] == "(" or compare (s [i], opt [-1]): # is high the current operator or a left parenthesis operator priority than the top of the stack, the stack operator directly opt
            opt.append(s[i])
                 else: # high priority than the operator stack, opt out from the stack while the stack data and computed results such as data stacks
            while opt and not compare(s[i], opt[-1]):
                                 if opt [-1] == "(": # If they are left parenthesis, calculation is stopped
                    break
                process(data, opt)
            opt.append(s[i])
                 After # i + 1 = index traverse shift
    while opt:
        process(data, opt)
    print(data.pop())
 
 
if __name__ == '__main__':
    exp = "(9+((3-1)*3+10/2))*2"
    calculate(exp)
 
