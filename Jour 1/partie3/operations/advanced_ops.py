def multiply(a: int, b: int) -> int:
    return a * b

def safe_divide(a: int, b: int) -> float | None:
    if b == 0:
        return None
    return a / b