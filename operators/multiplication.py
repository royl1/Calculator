from operators import operator


@operator.Operator.register_operator
class Multiplication(operator.Operator):
    """
        The multiplication operator, this operator allows us to multiplication one number from the other
    """
    def __init__(self):
        super().__init__('-')

    def act(self, x: int, y: int) -> int:
        return x * y
