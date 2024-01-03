'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

# First Solution - time O(N), space O(3N)
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowel = []
    ind = []
    new_str = []
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            vowel.append(s[i])
            ind.append(i)
        else:
            new_str.append(s[i])
    
    vowel_rev = vowel[::-1]
    print(vowel_rev)

    for i, x in enumerate(ind):
        new_str.insert(x, vowel_rev[i])
    return "".join(new_str)

# Second Solution - time O(N), space O(N)
# using stack
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """ 
    stack = []
    s = list(s)
    for c in s:
        if c in "aeiouAEIOU":
            stack.append(c)
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            s[i] = stack.pop()
    return "".join(s)

# Final Solution - time O(N), space O(1)
# using two pointers
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """ 
    s = list(s)
    vowels = 'aeiouAEIOU'
    l, r = 0, len(s)-1
    while l < r:
        while s[l] not in vowels and l < r:
            l += 1
        while s[r] not in vowels and l < r:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)