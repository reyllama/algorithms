"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1

        def isPalindrome(seq):
            if len(seq) == 0:
                return False
            if seq == seq[::-1]:
                return len(seq)
            return isPalindrome(seq[1:]) or isPalindrome(seq[:-1])

        return max(ans, isPalindrome(s))

'''
이렇게 코드를 짜면 DFS가 되어서 본 문제에서는 효율이 크게 떨어지게 된다. -> make it BFS
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        N = len(s)
        while N>1:
            for i in range(len(s)-N+1):
                if s[i:i+N] == s[i:i+N:-1]:
                    return N
            N -= 1
        return 1

'''
나름대로 BFS를 구현해봤는데, 최선인지는 잘 모르겠다. Solution 참고하자.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        cache = [[False]*N for _ in range(N)] # N x N grid
        for diag in range(len(cache)):
            cache[diag][diag] = True
        ans = s[-1]
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    if i+1 > j-1 or cache[i+1][j-1]:
                        ans = s[i:j+1] if j+1-i > len(ans) else ans
                        cache[i][j] = True
        return ans

'''
이렇게 cached DP로 접근하면 메모리는 더 쓰지만 보다 시간-효율적으로 답을 구할 수 있다.
'''