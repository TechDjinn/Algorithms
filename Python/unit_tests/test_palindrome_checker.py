from palindrome_checker import isPalindrome

# "Anna"
assert(isPalindrome("Anna")) == True, "Anna"
assert(isPalindrome("Anna", False, True)) == True, "Anna"
assert(isPalindrome("Anna", True, False)) == False, "Anna"
assert(isPalindrome("Anna", True, True)) == False, "Anna"
assert(isPalindrome("Anna", False, False)) == True, "Anna"

# "ABC c BA"
assert(isPalindrome("ABC c BA")) == True, "ABC c BA"
assert(isPalindrome("ABC c BA", False, True)) == True, "ABC c BA"
assert(isPalindrome("ABC c BA", True, False)) == False, "ABC c BA"
assert(isPalindrome("ABC c BA", True, True)) == False, "ABC c BA"
assert(isPalindrome("ABC c BA", False, False)) == False, "ABC c BA"

# Non-Palindrome
non_palindrome = ["hanna", "123", 123, " xy", 
                  "yx ", "abcdefg", 112233221,
                  "", "hercules", "j O s j"]
for element in non_palindrome:
    assert(isPalindrome(element)) == False, "non_palindrome"
    assert(isPalindrome(element, False, True)) == False, "non_palindrome"
    assert(isPalindrome(element, True, False)) == False, "non_palindrome"
    assert(isPalindrome(element, True, True)) == False, "non_palindrome"
    assert(isPalindrome(element, False, False)) == False, "non_palindrome"