def intersection(arrays):
    """
    YOUR CODE HERE
    """
    no_dupes = {}
    dupes = []
    
    for array in arrays:
        for num in array:
            if num in no_dupes and num not in dupes:
                dupes.append(num)
            else:
                no_dupes[num] = "ok"
    return dupes


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
