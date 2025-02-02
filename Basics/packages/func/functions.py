"""_summary_

    Returns:
        _type_: _description_
 """
import random


def rand_gen(x, y, z=False, w=1):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
        z (bool, optional): _description_. Defaults to False.
        w (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    arr = [random.randint(w, y) for i in range(x)]
    return sorted(arr) if z else arr
