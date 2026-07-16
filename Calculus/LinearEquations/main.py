# Solve the equation 3x-(x-7) = 4x-5

def evaluate(x):
    left_side = (3 * x) - (x - 7) 
    right_side = (4 * x) - 5

    if left_side == right_side:
        print(f"{x} is a solution to the equation")
    else:
        print(f"{x} is not a solution to the equation")


def main():
    x = int(input('Please enter a value for x to evaluate the expression 3x-(x-7) = 4x-5 :  '))
    evaluate(x)

main()