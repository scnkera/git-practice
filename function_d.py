def max_value(numbers):
    largest_number = 0
    """ This function returns the largest number
        in the list.
    """
    largest_number = max(numbers)
    
    return largest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
