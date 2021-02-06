"""An example function definition."""


def my_max(a: int, b:int) -> int: #this first line is called the "signature" or "contract"
    """Returns the largest argument""" #docstring
    if a>=b:
        return a
    else:
        return b     #from "if" to "return b" is the BODY BLOCK

print(my_max(11, 10))