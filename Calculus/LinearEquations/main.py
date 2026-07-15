# Solve the equation 3x-(x-7) = 4x-5

def evaluate(x):
    left_side = (3 * x) - (x - 7) 
    right_side = (4 * x) - 5
    
    print(f"Left Side: {left_side}")
    print(f"Right Side: {right_side}")

    print(f"Is left side equal to right side: {left_side == right_side}")

evaluate(6)