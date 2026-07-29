class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = {}
        second_word = {}
        for word in s:
            first_word[word] = s.count(word)
        for word in t:
            second_word[word] = t.count(word)
        return first_word == second_word        