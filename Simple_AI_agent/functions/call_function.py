import os


def call_function(function_call_part, verbose=False):
    """
    Simulates a function call by printing the function call part.
    If verbose is True, it prints additional information.
    """
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
