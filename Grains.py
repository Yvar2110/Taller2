def square(number):
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)
def total():
    return (2 << 63) - 1