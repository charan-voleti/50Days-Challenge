class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        rev=words[::-1]
        return ' '.join(rev)
    
        