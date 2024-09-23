def max_value(numbers):
    largest_number = 0
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return(largest_number)
=======
    return max(numbers)
>>>>>>> 1b23a66e0535c314d41dce518efe6d9c02503b62


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
