# O(n^2) Time | O(n) Space
# def isPalindrome(string):
#     new=""
#     for i in reversed(range(len(string))):
#         new+=string[i]
#     return new==string

# O(n) Time | O(n) Space
# def isPalindrome(string):
#     newword =[]
#     for i in reversed(range(len(string))):
#         newword.append(string[i])
#     return string == ''.join(newword)
#

# O(n) Time | O(n) Space Tail recursion but still uses call stack leading to O(n) Space
# def isPalindrome(string,i=0):

#     j= len(string)-1-i
#     if i>=j:
#         return True
#     if string[i]!=string[j]:
#         return False
#     return isPalindrome(string,i+1)

# O(n) Time | O(1) Space


def isPalindrome(string):

    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print(isPalindrome('abc4a'))
