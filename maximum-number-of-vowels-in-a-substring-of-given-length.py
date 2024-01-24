'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length
'''

# Solution 1: this solution won't work, it will hit a time limit error buecause it needs further optimization.
def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # vowels = set('aeiou')
        # cnt=0
        # for i in range(len(s)-k+1):
        #     win = s[i:i+k]
        #     temp_cnt = 0
        #     for x in vowels.intersection(set(win)):
        #         temp_cnt+=win.count(x)
        #     if temp_cnt > cnt:
        #         cnt = temp_cnt
        # return cnt

# Solution 2:(best solution)
def maxVowels(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    vowel = 'aeiou'
    win = s[:k]
    cnt=0
    for x in win:
        if x in vowel:
            cnt+=1
    max_cnt = cnt

    for i in range(len(s)-k):
        if s[i] in 'aeiou':
            cnt-=1
        if s[i+k] in 'aeiou':
            cnt+=1
        if cnt>max_cnt:
            max_cnt = cnt
    return max_cnt 