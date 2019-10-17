import ast
from operator import add, mul, neg, sub, truediv


# Using SymPy is also an option to concider

ops = {ast.Add : add,
       ast.Sub : sub,
       ast.Mult: mul,
       ast.Div : truediv,
       ast.USub: neg
       }


def parse(node):
    global ops
    
    if isinstance(node, ast.Num):  # <number>
        return node.n
    
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return ops[type(node.op)](parse(node.left), parse(node.right))
    
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return ops[type(node.op)](parse(node.operand))
    
    else:
        raise TypeError(node)


def calculate_expr(expression):
    return parse(ast.parse(expression, mode='eval').body)


def test_strings():
    ex0 = '2 + 3'  # 5
    ex1 = '1 + 2 * 3'  # 7
    ex2 = '(-40 + 2 * 14) / -2'  # 6
    ex3 = '(2 + 3) * (2 * 6 / 4) - 1'  # 14
    ex4 = '(2 + 4 *(100 - 90) + 3) / -5'  # -9
    ex5 = '(100 - 99.9) * 10'  # 1
    
    ex = ex0, ex1, ex2, ex3, ex4, ex5
    
    for e in ex:
        print(e, calculate_expr(e), sep='\t\t')
