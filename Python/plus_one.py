def plusOne(digits):
    """
    Description:
        Increment the number, represented as a list, by one.

    Argument:
        A number, represented as a list.
        ( e.g. digits = [3, 6, 9] )

    Return:
        A list, where the digit has been incremented by one.
        ( e.g. digits = [3, 7, 0] )
    """
    j = len(digits) - 1
    # If the least significants are 9's; 
    # we need to start where the nines ends.
    # If there is no nines there; this loop will be skiped.
    while digits[j] == 9:
        if j == 0:
            # If all are nines, we need another digit. (new power of ten)
            digits = [0] + digits
            break
        j -= 1
    
    # Increment the number (least significant none-nine)
    digits[j] += 1
    j += 1

    # Change the nines to zero.
    while j < len(digits):
        digits[j] = 0
        j += 1

    return digits