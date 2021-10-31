def find_if_bracketing_is_valid(S):
    stack_of_brackets = []
    for x in S:
        if x in ["{","[","("]:
            stack_of_brackets.append(x)
        elif x == "}":
            if "{" != stack_of_brackets.pop():
                return 0
        elif x == "]":
            if "[" != stack_of_brackets.pop():
                return 0
        elif x == ")":
            if "(" != stack_of_brackets.pop():
                return 0
    return 1
