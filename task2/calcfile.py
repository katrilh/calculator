import ast
from operator import add, mul, neg, sub, truediv


# I concidered using the SymPy libary for handling the arithmetic.
# SymPy can handle more advanced mathematics, but at the cost of being slower

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


if __name__ == '__main__':
    calculate_expr('')
    
