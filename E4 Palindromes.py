

def find_palindromes(bottom: int, top: int):
    palindromes = []
    for n in range(top, bottom-1, -1):
        if str(n) == str(n)[::-1]:
            palindromes.append(n)
    return palindromes

def divisible_in_range(value: int, bottom: int, top: int):
    for n in range(bottom, top+1):
        if value % n == 0 and clamped(int(value/n), bottom, top):
            return True
    return False

def clamped(value: int, bottom: int, top: int):
    return value >= bottom and value <= top


for palindrome in find_palindromes(100**2, 999**2):
    if divisible_in_range(palindrome, 100, 999):
        print(palindrome)
        break
