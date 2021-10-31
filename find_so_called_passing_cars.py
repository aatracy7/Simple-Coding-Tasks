def find_so_called_passing_cars(A):
    #This really finds the sum of the sum of 0s before each 1 in an array of 1s and 0s
    n = len(A)
    prefix_sums = [0] * (n + 1)
    east_cars = 0
    already_passed = 0
    for k in range(1, n+1):
        prefix_sums[k] = prefix_sums[k-1] + A[k-1]
    for i, x in enumerate(prefix_sums[1:]):
        if x == prefix_sums[i]:
            east_cars += 1
            already_passed += x
    total_passing_cars = east_cars * prefix_sums[-1] - already_passed
    if total_passing_cars > 1000000000:
        return -1
    else:
        return total_passing_cars
