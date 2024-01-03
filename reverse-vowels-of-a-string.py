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