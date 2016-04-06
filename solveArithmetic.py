def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

def add(a,b):
    return a+b

funcDict= {
    '*' : mult,
    '/' : div,
    '+' : add,
    '-' : sub
    }

def evaluate(a,b, op):
    func = funcDict[op]
    return func(a,b)

# clean input: operand + [operator + operand] *
def main(expression):
    l1 = [int(x) if x.isdigit() else x for x in expression.split()]
    if len(l1) < 1:
        return None
    l1.reverse()
    l2 = []
    while (len(l1)>1):
        operand1 = l1.pop()
        operator = l1.pop()
        operand2 = l1.pop()

        if operator == '*' or operator == '/':
            l1.append(evaluate(operand1, operand2, operator))
        elif operator == '+' or operator == '-':
            l2.append(operand1)
            l2.append(operator)
            l1.append(operand2)
        else:
            pass
    l2.append(l1[0])
    l2.reverse()

    while (len(l2)>2):
        operand1 = l2.pop()
        operator = l2.pop()
        operand2 = l2.pop()
        if operator == '+' or operator == '-':
            l2.append(evaluate(operand1, operand2, operator))
        else:
            pass
    return l2[0]
