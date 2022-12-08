"""Write custom str to int conversion."""
# This inludes only for +ve numbers. For -ve we need to start from position 1 instead of 0 and mulitply by -1 at the end)
# We are going to python's `ord()` function
def str_to_int(number_str: str) -> int:
    length = len(number_str)
    output=0
    for i in range(length):
        digit = (ord(number_str[i]) - 48)
        digit_place = 10**(length -(i+1)) 
        output += digit_place * digit
    return output

print(str_to_int("12359"))
