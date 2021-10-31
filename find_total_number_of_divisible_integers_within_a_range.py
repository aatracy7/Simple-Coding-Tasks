def find_total_number_of_divisible_integers_within_a_range(A,B,K):
    #A is the start of a range, B is the end, K is the number to check for divisibility
    #The total possible numbers divisible by K is really close to the range's size divided by K.
    #One just has to see if the range falls in such a way as to add one more or not
    total_possible = (B-A)/K #approximate for now
    the_remainder =  (B-A) % K
    if the_remainder  == 0:
        if A % K == 0:
            total_possible += 1
        return int(total_possible)
    else:
        for i in range(A, A + (the_remainder * K + 1)):
            if i % K == 0:
                total_possible = floor(total_possible) + 1
    return total_possible
