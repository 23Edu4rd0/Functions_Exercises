def is_leap_year(year):
    """
    says if a year is a lean year or not
    to know if a year is a leap year, he has to be divided by 4, can't be divided by 100, except if him is divide by 400
    """
    divisible4 = year % 4
    divisible100 = year % 100
    divisible400 = year % 400
    print(f"Divisible by 4: {divisible4 == 0}")
    print(f"Divisible by 100: {divisible100 == 0}")
    print(f"Divisible by 400: {divisible400 == 0}")
    if divisible4 == 0 and (divisible100 != 0 or divisible400 == 0):
        return True
    else :
        return False
# Insert the year here: 
print (is_leap_year(1900))
