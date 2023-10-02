def multiple(number):
    if number % 5 == 0 and number % 7 == 0:
        return "fizzbuzz"

    if number % 7 == 0:
        return "buzz"

    if number % 5 == 0:
        return "fizz"

    return "miss"