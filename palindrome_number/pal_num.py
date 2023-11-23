some_num = 1771


def is_palindrome(num):
    reversed_num = str(num)[::-1]
    return str(num) == reversed_num
