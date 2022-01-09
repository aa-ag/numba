############------------ IMPORTS ------------############
from time import time, sleep
from numba import jit
from numba.core.decorators import njit


############------------ FUNCTION(S) ------------############

def example_function():
    '''
     took: 105.74 seconds
    '''
    expected_result = list()

    for x in range(100):
        for y in range(1000):
            for z in range(10000):
                if (x + y + z) / 10 == x:
                    expected_result.append(x)
        print(x)
    return expected_result


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    start_time = time()
    example_function()
    print(f"took: {round(time() - start_time, 2)} seconds")