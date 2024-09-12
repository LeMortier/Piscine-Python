from operations import add, subtract, multiply, safe_divide

def do_op(a: int, b: int, op: str) -> float | int | None:
    match op:
        case '+':
            return add(a, b)
        case '-':
            return subtract(a, b)
        case '*':
            return multiply(a, b)
        case '/':
            return safe_divide(a, b)
        case _:
            return None
