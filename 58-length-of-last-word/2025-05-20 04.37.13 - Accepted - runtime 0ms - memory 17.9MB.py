class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length_last_word = 0
        first_char_found = False

        while i >= 0:
            if s[i] != " ":
                first_char_found = True
                length_last_word += 1
            elif first_char_found:
                break
            i -= 1

        return length_last_word
