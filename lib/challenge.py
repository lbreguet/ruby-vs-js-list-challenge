# Requirements


# Add your function parameters between the parentheses.
def challenge_any(array, predicate):
    return any(map(predicate, array))


# Add your function parameters between the parentheses.
def challenge_none(array, predicate):
    return len(list(filter(lambda e: e, map(predicate, array)))) == 0

# Bonuses


# Add your function parameters between the parentheses.
def challenge_one(array, predicate):
    return len(list(filter(lambda e: e, map(predicate, array)))) == 1


# Add your function parameters between the parentheses.
def challenge_all(array, predicate):
    return len(list(filter(lambda e: e, map(predicate, array)))) == len(array)
