def has_negatives(a):
    """
    YOUR CODE HERE
    """
    negative = []
    positive = {}
    solution = []
    # Your code here
    for num in a:
        if num < 0:
            negative.append(num)
        else:
            positive[num] = num
    for number in negative:
        if abs(number) in positive:
            solution.append(positive[abs(number)])
    return solution

    
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
