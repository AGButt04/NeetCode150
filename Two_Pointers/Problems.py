# This file has all the problems in the Two Pointers
# section of the NeetCode150 with the explanations.

import string

def isPalindrome(s):
    st = s.replace(' ', '')
    st = st.lower()
    translator = str.maketrans('', '', string.punctuation)
    st = st.translate(translator)
    left = 0
    right = len(st) - 1

    while left < right:
        char = st[left]
        ch = st[right]
        if char != ch:
            return False

        left += 1
        right -= 1

    return True



if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    print(isPalindrome(s))