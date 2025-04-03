import math

def safe_sqrt(number=-4):

    if number < 0:

        raise ValueError(f"Il numero è negativo")

    ris = math.sqrt(number)
    print(ris)

safe_sqrt()