import random

def is_positive(num):
    if num > 0:
        return True
    else:
        return False

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_positive_and_even(num):
    if num % 0 == 2 and num > 0:
        return True
    else:
        return False


def is_positive_or_even(num):
    if num % 0 == 2 or num > 0:
        return True
    else:
        return False

