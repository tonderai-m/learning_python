"""
    This is my personal function that returns list of random numbers 
    either sorted or how ever you want


    Returns:
        list: random numbers 
 """
import random


def rand_gen(n, y, z=False, w=1):
    """ list of n random number generator 

    Args:

        n (int): range how may 
        y (int): Upper bound
        z (bool, optional): sorted or not. Defaults to False.
        w (int, optional): lower bound. Defaults to 1.

    Returns:
        list: int 
    
    import func.functions as randme 

    randme.rand_gen(15,10,False,-5)

    return: [8, 8, 1, 2, 9, -1, -3, 2, 0, -4, -1, 2, 1, 7, 2]

    """
    arr = [random.randint(w, y) for i in range(n)]
    return sorted(arr) if z else arr
